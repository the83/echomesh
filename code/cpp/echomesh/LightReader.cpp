#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>

#include "echomesh/LightComponent.h"
#include "echomesh/LightReader.h"

namespace echomesh {

using namespace std;

static const char DEVICE_NAME[] = "/dev/spidev0.0";
const int LATCH_BYTE_COUNT = 3;
uint8 LATCH[LATCH_BYTE_COUNT] = {0};

LightReader::LightReader(LightComponent* light, const String& commandLine)
    : ReadThread(commandLine),
      lightComponent_(light)
#if JUCE_LINUX
, file_(fopen(DEVICE_NAME, "w"))
#endif
{
}

LightReader::~LightReader() {
#if JUCE_LINUX
  fclose(file_);
#endif
}

void LightReader::parseNode() {
  log("parseNode " + type_);
  if (type_ == "clear")
    clear();
  else if (type_ == "config")
    parseConfig();
  else if (type_ == "light")
    parseLight();
  else if (type_ == "quit")
    quit();
  else
    log("Didn't understand type " + type_);
}

void LightReader::quit() {
  log("Program quitting");
  signalThreadShouldExit();
  // JUCEApplication::getInstance()->systemRequestedQuit();
  JUCEApplication::quit();
  log("quit done.");
  close_log();
}

void LightReader::clear() {
  for (int i = 0; i < colors_.size(); ++i)
    colors_[i] = Colours::black;

  displayLights();
  log("clear done ");
}

void LightReader::enforceSizes() {
  if (colors_.size() != config_.count)
    colors_.resize(config_.count, Colours::black);

  if (colorBytes_.size() != 3 * config_.count)
    colorBytes_.resize(3 * config_.count, 0x80);
}

#define WHICH_RGB true

void LightReader::parseConfig() {
  const YAML::Node& data = node_["data"];
  log("parseConfig.");
  data >> config_;
  enforceSizes();

  for (int i = 0; i < 3; ++i) {
#if WHICH_RGB
    rgb_order_[i] = config_.rgb_order.find("rgb"[i]);
#else
    rgb_order_[i] = string("rgb").find(config_.rgb_order[i]);
#endif
  }
  log("set config set light.");
  lightComponent_->setConfig(config_);
  log("parseConfig done.");
}

uint8 LightReader::getLedColor(float color) const {
  int c = static_cast<int>((color * brightness_ + 1) * 0x80);
  return static_cast<uint8>(jmin(c, 0xFF));
}

void LightReader::parseLight() {
  const YAML::Node& data = node_["data"];
  log("parseLight...");
  data["colors"] >> colors_;
  data["brightness"] >> brightness_;
  enforceSizes();
  displayLights();
  log("parseLight done...");
}

void LightReader::displayLights() {
  for (int i = 0; i < config_.count; ++i) {
    const Colour& color = colors_[i];
    uint8* light = &colorBytes_[3 * i];
    light[rgb_order_[0]] = getLedColor(color.getFloatRed());
    light[rgb_order_[1]] = getLedColor(color.getFloatGreen());
    light[rgb_order_[2]] = getLedColor(color.getFloatBlue());
  }

#if JUCE_LINUX
  fwrite(&colorBytes_.front(), 1, colorBytes_.size(), file_);
  fflush(file_);
  fwrite(LATCH, 1, 3, file_);
  fflush(file_);
#endif
  log("about to setlights...");
  lightComponent_->setLights(colors_);
  log("displayLights done.");
}

}  // namespace echomesh
