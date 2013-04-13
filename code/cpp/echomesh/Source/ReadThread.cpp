#include "/development/echomesh/code/cpp/echomesh/Source/ReadThread.h"

#include "LightComponent.h"

#include <iostream>
#include <string>
#include <stdio.h>

namespace echomesh {

using namespace std;

static const char DEVICE_NAME[] = "/dev/spidev0.0";
const int LATCH_BYTE_COUNT = 3;
uint8 LATCH[LATCH_BYTE_COUNT] = {0};
const char READ_FILE[] = "/development/echomesh/incoming.data";

ReadThread::ReadThread(LightComponent* light)
    : Thread("ReadThread"), lightComponent_(light), stream_(&std::cin)
#if JUCE_LINUX
, file_(fopen(DEVICE_NAME, "w"))
#endif
{
}

ReadThread::~ReadThread() {
#if JUCE_LINUX
  fclose(file_);
#endif
}

void ReadThread::run() {
  string s;
  String st;
  while (!stream_->eof()) {
    s.clear();
    getline(*stream_, s);
    if (s.find("---"))
      accum_.add(s.c_str());
    else
      handleMessage();
  }
}

void ReadThread::handleMessage() {
  String result = accum_.joinIntoString("\n");
  accum_.clear();
  std::string str(result.toUTF8());
  std::istringstream s(str);
  try {
    YAML::Parser parser(s);
    if (parser.GetNextDocument(node_))
      parseNode();
  } catch (YAML::Exception& e) {
    std::cout << e.what() << "\n";
    std::cout << result << "\n";
  }
}

void ReadThread::parseNode() {
  std::string type;
  node_["type"] >> type;
  if (type == "clear")
    clear();
  else if (type == "config")
    parseConfig(node_["data"]);
  else if (type == "light")
    parseLight(node_["data"]);
  else if (type == "quit")
    quit();
}

void ReadThread::quit() {
  signalThreadShouldExit();
  JUCEApplication::quit();
  exit(0);
}

void ReadThread::clear() {
  for (int i = 0; i < colors_.size(); ++i)
    colors_[i] = Colours::black;

  displayLights();
}

void ReadThread::enforceSizes() {
  if (colors_.size() != config_.count)
    colors_.resize(config_.count, Colours::black);

  if (colorBytes_.size() != 3 * config_.count)
    colorBytes_.resize(3 * config_.count, 0x80);
}

#define WHICH_RGB true

void ReadThread::parseConfig(const YAML::Node& data) {
  return;
  data >> config_;
  enforceSizes();

  for (int i = 0; i < 3; ++i) {
#if WHICH_RGB
    rgb_order_[i] = config_.rgb_order.find("rgb"[i]);
#else
    rgb_order_[i] = string("rgb").find(config_.rgb_order[i]);
#endif
  }
  lightComponent_->setConfig(config_);
}

static uint8 process(uint8 color, double brightness) {
  int c = static_cast<int>(color * brightness / 2 + 0x80);
  return static_cast<uint8>(jmin(c, 0xFF));
}

void ReadThread::parseLight(const YAML::Node& data) {
  data["colors"] >> colors_;
  data["brightness"] >> brightness_;
  enforceSizes();
  displayLights();
}

void ReadThread::displayLights() {
  for (int i = 0; i < config_.count; ++i) {
    const Colour& color = colors_[i];
    uint8* light = &colorBytes_[3 * i];
    light[rgb_order_[0]] = process(color.getRed(), brightness_);
    light[rgb_order_[1]] = process(color.getGreen(), brightness_);
    light[rgb_order_[2]] = process(color.getBlue(), brightness_);
  }

#if JUCE_LINUX
  fwrite(&colorBytes_.front(), 1, colorBytes_.size(), file_);
  fflush(file_);
  fwrite(LATCH, 1, 3, file_);
  fflush(file_);
#endif
  lightComponent_->setLights(colors_);
}

}  // namespace echomesh