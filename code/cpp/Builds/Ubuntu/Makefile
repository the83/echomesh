# Automatically generated makefile, created by the Introjucer
# Don't edit this file! Your changes will be overwritten when you re-save the Introjucer project!

# (this disables dependency generation if multiple architectures are set)
DEPFLAGS := $(if $(word 2, $(TARGET_ARCH)), , -MMD)

ifndef CONFIG
  CONFIG=Debug
endif

ifeq ($(CONFIG),Debug)
  BINDIR := build
  LIBDIR := build
  OBJDIR := build/intermediate/Debug
  OUTDIR := build

  ifeq ($(TARGET_ARCH),)
    TARGET_ARCH := -march=native
  endif

  CPPFLAGS := $(DEPFLAGS) -D "LINUX=1" -D "DEBUG=1" -D "_DEBUG=1" -D "JUCE_DISABLE_JUCE_VERSION_PRINTING=1" -D "JUCER_LINUX_MAKE_4907871=1" -I /usr/include -I /usr/include/freetype2 -I ../../JuceLibraryCode -I ../../JuceLibraryCode/modules
  CFLAGS += $(CPPFLAGS) $(TARGET_ARCH) -g -ggdb -O0 -I../.. -I../../build/include -std=c++11 -stdlib=libc++ -fPIC
  CXXFLAGS += $(CFLAGS)
  LDFLAGS += $(TARGET_ARCH) -L$(BINDIR) -L$(LIBDIR) -L/usr/X11R6/lib/ -lX11 -lXext -lXinerama -lasound -ldl -lfreetype -lpthread -lrt -lglog -L../../build/lib
  LDDEPS :=
  RESFLAGS :=  -D "LINUX=1" -D "DEBUG=1" -D "_DEBUG=1" -D "JUCE_DISABLE_JUCE_VERSION_PRINTING=1" -D "JUCER_LINUX_MAKE_4907871=1" -I /usr/include -I /usr/include/freetype2 -I ../../JuceLibraryCode -I ../../JuceLibraryCode/modules
  TARGET := libechomesh.a
  BLDCMD = ar -rcs $(OUTDIR)/$(TARGET) $(OBJECTS)
endif

ifeq ($(CONFIG),Release)
  BINDIR := build
  LIBDIR := build
  OBJDIR := build/intermediate/Release
  OUTDIR := build

  ifeq ($(TARGET_ARCH),)
    TARGET_ARCH := -march=native
  endif

  CPPFLAGS := $(DEPFLAGS) -D "LINUX=1" -D "NDEBUG=1" -D "JUCE_DISABLE_JUCE_VERSION_PRINTING=1" -D "JUCER_LINUX_MAKE_4907871=1" -I /usr/include -I /usr/include/freetype2 -I ../../JuceLibraryCode -I ../../JuceLibraryCode/modules
  CFLAGS += $(CPPFLAGS) $(TARGET_ARCH) -Os -I../.. -I../../build/include -std=c++11 -stdlib=libc++ -fPIC
  CXXFLAGS += $(CFLAGS)
  LDFLAGS += $(TARGET_ARCH) -L$(BINDIR) -L$(LIBDIR) -fvisibility=hidden -L/usr/X11R6/lib/ -lX11 -lXext -lXinerama -lasound -ldl -lfreetype -lpthread -lrt -lglog -L../../build/lib
  LDDEPS :=
  RESFLAGS :=  -D "LINUX=1" -D "NDEBUG=1" -D "JUCE_DISABLE_JUCE_VERSION_PRINTING=1" -D "JUCER_LINUX_MAKE_4907871=1" -I /usr/include -I /usr/include/freetype2 -I ../../JuceLibraryCode -I ../../JuceLibraryCode/modules
  TARGET := libechomesh.a
  BLDCMD = ar -rcs $(OUTDIR)/$(TARGET) $(OBJECTS)
endif

OBJECTS := \
  $(OBJDIR)/base64_1eb4a3a4.o \
  $(OBJDIR)/AudioPlayer_4a16e216.o \
  $(OBJDIR)/AudioController_2cdb5551.o \
  $(OBJDIR)/DefaultDevice_d5d51936.o \
  $(OBJDIR)/Envelope_e091de3b.o \
  $(OBJDIR)/EnvelopeValuePlayer_308b601.o \
  $(OBJDIR)/GetReader_4ae00cf8.o \
  $(OBJDIR)/MidiController_f87aad08.o \
  $(OBJDIR)/SampleAudioSource_602b6bc6.o \
  $(OBJDIR)/Source_b9c08e86.o \
  $(OBJDIR)/Config_4a6afa38.o \
  $(OBJDIR)/Log_edbe3e58.o \
  $(OBJDIR)/InstrumentComponent_75edd5bc.o \
  $(OBJDIR)/InstrumentGrid_18eea031.o \
  $(OBJDIR)/LightingWindow_79bb5b00.o \
  $(OBJDIR)/Echomesh_ddd28324.o \
  $(OBJDIR)/Main_ed86ae4b.o \
  $(OBJDIR)/LightController_57a59429.o \
  $(OBJDIR)/LightReader_649349d0.o \
  $(OBJDIR)/LineGetter_4e1cc2f2.o \
  $(OBJDIR)/ReadThread_1a08d793.o \
  $(OBJDIR)/SocketLineGetter_649dfac5.o \
  $(OBJDIR)/InitLog_83a5ff59.o \
  $(OBJDIR)/EchomeshApplication_68207ea3.o \
  $(OBJDIR)/FastTrig_b97710bd.o \
  $(OBJDIR)/GetDevice_bdff9491.o \
  $(OBJDIR)/Manager_ac61fac2.o \
  $(OBJDIR)/RegisterFormats_a3caa84e.o \
  $(OBJDIR)/OutputSampleRate_b96311f8.o \
  $(OBJDIR)/Trash_ed189496.o \
  $(OBJDIR)/aliasmanager_6b830d0d.o \
  $(OBJDIR)/binary_6a84dff1.o \
  $(OBJDIR)/graphbuilder_3e9247f3.o \
  $(OBJDIR)/graphbuilderadapter_403d2f86.o \
  $(OBJDIR)/conversion_51b63106.o \
  $(OBJDIR)/directives_a829c6f4.o \
  $(OBJDIR)/emitfromevents_d2126bc6.o \
  $(OBJDIR)/emitter_919ca4c8.o \
  $(OBJDIR)/emitterstate_f549893.o \
  $(OBJDIR)/emitterutils_d22dd4b3.o \
  $(OBJDIR)/exp_ff0c1e77.o \
  $(OBJDIR)/iterator_3b9f5b1e.o \
  $(OBJDIR)/node_9bbecc32.o \
  $(OBJDIR)/nodebuilder_271e7cb3.o \
  $(OBJDIR)/nodeownership_5e4951c7.o \
  $(OBJDIR)/null_e72d9937.o \
  $(OBJDIR)/ostream_8adb6189.o \
  $(OBJDIR)/parser_6588d10f.o \
  $(OBJDIR)/regex_c10dea61.o \
  $(OBJDIR)/scanner_dc701758.o \
  $(OBJDIR)/scanscalar_1b773f19.o \
  $(OBJDIR)/scantag_126715d7.o \
  $(OBJDIR)/scantoken_f539c6b6.o \
  $(OBJDIR)/simplekey_565ab407.o \
  $(OBJDIR)/singledocparser_509dffe9.o \
  $(OBJDIR)/stream_57c84bf0.o \
  $(OBJDIR)/tag_f0cb4d74.o \
  $(OBJDIR)/juce_audio_basics_2442e4ea.o \
  $(OBJDIR)/juce_audio_devices_a4c8a728.o \
  $(OBJDIR)/juce_audio_formats_d349f0c8.o \
  $(OBJDIR)/juce_core_aff681cc.o \
  $(OBJDIR)/juce_cryptography_25c7e826.o \
  $(OBJDIR)/juce_data_structures_bdd6d488.o \
  $(OBJDIR)/juce_events_79b2840.o \
  $(OBJDIR)/juce_graphics_c8f1e7a4.o \
  $(OBJDIR)/juce_gui_basics_a630dd20.o \
  $(OBJDIR)/juce_gui_extra_7767d6a8.o \

.PHONY: clean

$(OUTDIR)/$(TARGET): $(OBJECTS) $(LDDEPS) $(RESOURCES)
	@echo Linking echomesh
	-@mkdir -p $(BINDIR)
	-@mkdir -p $(LIBDIR)
	-@mkdir -p $(OUTDIR)
	@$(BLDCMD)

clean:
	@echo Cleaning echomesh
	-@rm -f $(OUTDIR)/$(TARGET)
	-@rm -rf $(OBJDIR)/*
	-@rm -rf $(OBJDIR)

strip:
	@echo Stripping echomesh
	-@strip --strip-unneeded $(OUTDIR)/$(TARGET)

$(OBJDIR)/base64_1eb4a3a4.o: ../../base64/base64.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling base64.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/AudioPlayer_4a16e216.o: ../../echomesh/audio/AudioPlayer.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling AudioPlayer.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/AudioController_2cdb5551.o: ../../echomesh/audio/AudioController.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling AudioController.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/DefaultDevice_d5d51936.o: ../../echomesh/audio/DefaultDevice.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling DefaultDevice.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/Envelope_e091de3b.o: ../../echomesh/audio/Envelope.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling Envelope.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/EnvelopeValuePlayer_308b601.o: ../../echomesh/audio/EnvelopeValuePlayer.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling EnvelopeValuePlayer.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/GetReader_4ae00cf8.o: ../../echomesh/audio/GetReader.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling GetReader.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/MidiController_f87aad08.o: ../../echomesh/audio/MidiController.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling MidiController.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/SampleAudioSource_602b6bc6.o: ../../echomesh/audio/SampleAudioSource.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling SampleAudioSource.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/Source_b9c08e86.o: ../../echomesh/audio/Source.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling Source.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/Config_4a6afa38.o: ../../echomesh/base/Config.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling Config.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/Log_edbe3e58.o: ../../echomesh/base/Log.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling Log.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/InstrumentComponent_75edd5bc.o: ../../echomesh/component/InstrumentComponent.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling InstrumentComponent.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/InstrumentGrid_18eea031.o: ../../echomesh/component/InstrumentGrid.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling InstrumentGrid.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/LightingWindow_79bb5b00.o: ../../echomesh/component/LightingWindow.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling LightingWindow.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/Echomesh_ddd28324.o: ../../echomesh/Echomesh.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling Echomesh.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/Main_ed86ae4b.o: ../../echomesh/Main.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling Main.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/LightController_57a59429.o: ../../echomesh/network/LightController.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling LightController.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/LightReader_649349d0.o: ../../echomesh/network/LightReader.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling LightReader.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/LineGetter_4e1cc2f2.o: ../../echomesh/network/LineGetter.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling LineGetter.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/ReadThread_1a08d793.o: ../../echomesh/network/ReadThread.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling ReadThread.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/SocketLineGetter_649dfac5.o: ../../echomesh/network/SocketLineGetter.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling SocketLineGetter.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/InitLog_83a5ff59.o: ../../echomesh/util/InitLog.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling InitLog.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/EchomeshApplication_68207ea3.o: ../../echomesh/util/EchomeshApplication.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling EchomeshApplication.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/FastTrig_b97710bd.o: ../../echomesh/util/FastTrig.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling FastTrig.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/GetDevice_bdff9491.o: ../../echomesh/util/GetDevice.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling GetDevice.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/Manager_ac61fac2.o: ../../rec/audio/format/Manager.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling Manager.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/RegisterFormats_a3caa84e.o: ../../rec/audio/format/RegisterFormats.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling RegisterFormats.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/OutputSampleRate_b96311f8.o: ../../rec/audio/OutputSampleRate.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling OutputSampleRate.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/Trash_ed189496.o: ../../rec/util/thread/Trash.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling Trash.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/aliasmanager_6b830d0d.o: ../../yaml-cpp-src/aliasmanager.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling aliasmanager.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/binary_6a84dff1.o: ../../yaml-cpp-src/binary.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling binary.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/graphbuilder_3e9247f3.o: ../../yaml-cpp-src/contrib/graphbuilder.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling graphbuilder.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/graphbuilderadapter_403d2f86.o: ../../yaml-cpp-src/contrib/graphbuilderadapter.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling graphbuilderadapter.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/conversion_51b63106.o: ../../yaml-cpp-src/conversion.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling conversion.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/directives_a829c6f4.o: ../../yaml-cpp-src/directives.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling directives.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/emitfromevents_d2126bc6.o: ../../yaml-cpp-src/emitfromevents.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling emitfromevents.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/emitter_919ca4c8.o: ../../yaml-cpp-src/emitter.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling emitter.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/emitterstate_f549893.o: ../../yaml-cpp-src/emitterstate.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling emitterstate.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/emitterutils_d22dd4b3.o: ../../yaml-cpp-src/emitterutils.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling emitterutils.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/exp_ff0c1e77.o: ../../yaml-cpp-src/exp.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling exp.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/iterator_3b9f5b1e.o: ../../yaml-cpp-src/iterator.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling iterator.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/node_9bbecc32.o: ../../yaml-cpp-src/node.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling node.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/nodebuilder_271e7cb3.o: ../../yaml-cpp-src/nodebuilder.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling nodebuilder.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/nodeownership_5e4951c7.o: ../../yaml-cpp-src/nodeownership.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling nodeownership.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/null_e72d9937.o: ../../yaml-cpp-src/null.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling null.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/ostream_8adb6189.o: ../../yaml-cpp-src/ostream.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling ostream.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/parser_6588d10f.o: ../../yaml-cpp-src/parser.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling parser.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/regex_c10dea61.o: ../../yaml-cpp-src/regex.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling regex.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/scanner_dc701758.o: ../../yaml-cpp-src/scanner.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling scanner.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/scanscalar_1b773f19.o: ../../yaml-cpp-src/scanscalar.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling scanscalar.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/scantag_126715d7.o: ../../yaml-cpp-src/scantag.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling scantag.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/scantoken_f539c6b6.o: ../../yaml-cpp-src/scantoken.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling scantoken.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/simplekey_565ab407.o: ../../yaml-cpp-src/simplekey.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling simplekey.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/singledocparser_509dffe9.o: ../../yaml-cpp-src/singledocparser.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling singledocparser.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/stream_57c84bf0.o: ../../yaml-cpp-src/stream.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling stream.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/tag_f0cb4d74.o: ../../yaml-cpp-src/tag.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling tag.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_audio_basics_2442e4ea.o: ../../JuceLibraryCode/modules/juce_audio_basics/juce_audio_basics.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_audio_basics.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_audio_devices_a4c8a728.o: ../../JuceLibraryCode/modules/juce_audio_devices/juce_audio_devices.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_audio_devices.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_audio_formats_d349f0c8.o: ../../JuceLibraryCode/modules/juce_audio_formats/juce_audio_formats.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_audio_formats.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_core_aff681cc.o: ../../JuceLibraryCode/modules/juce_core/juce_core.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_core.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_cryptography_25c7e826.o: ../../JuceLibraryCode/modules/juce_cryptography/juce_cryptography.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_cryptography.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_data_structures_bdd6d488.o: ../../JuceLibraryCode/modules/juce_data_structures/juce_data_structures.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_data_structures.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_events_79b2840.o: ../../JuceLibraryCode/modules/juce_events/juce_events.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_events.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_graphics_c8f1e7a4.o: ../../JuceLibraryCode/modules/juce_graphics/juce_graphics.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_graphics.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_gui_basics_a630dd20.o: ../../JuceLibraryCode/modules/juce_gui_basics/juce_gui_basics.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_gui_basics.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

$(OBJDIR)/juce_gui_extra_7767d6a8.o: ../../JuceLibraryCode/modules/juce_gui_extra/juce_gui_extra.cpp
	-@mkdir -p $(OBJDIR)
	@echo "Compiling juce_gui_extra.cpp"
	@$(CXX) $(CXXFLAGS) -o "$@" -c "$<"

-include $(OBJECTS:%.o=%.d)
