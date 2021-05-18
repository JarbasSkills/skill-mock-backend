# Mock Backend Skill

Disable mycroft from phoning home.mycroft.ai

![](./logo.png)


## About

Just install the skill and backend will be disabled

This is beta, some skills WILL break, see [OpenVoiceOS/OVOS-local-backend](https://github.com/OpenVoiceOS/OVOS-local-backend) for details

PRIVACY NOTE: you need to setup your own STT, by default it will use google

[kaldi](https://github.com/HelloChatterbox/speech2text/blob/dev/speech2text/engines/kaldi.py) and [deepspeech](https://github.com/HelloChatterbox/speech2text/blob/dev/speech2text/engines/ds.py) are supported


## Examples

* "restore mycroft backend"
* "disable mycroft backend"
* "what backend are you using"

# Platform support

- :heavy_check_mark: - tested and confirmed working
- :x: - incompatible/non-functional
- :question: - untested
- :construction: - partial support

|     platform    |   status   |  tag  | version | last tested | 
|:---------------:|:----------:|:-----:|:-------:|:-----------:|
|    [Chatterbox](https://hellochatterbox.com)   | :question: |  dev  |         |    never    | 
|     [HolmesV](https://github.com/HelloChatterbox/HolmesV)     | :question: |  dev  |         |    never    | 
|    [LocalHive](https://github.com/JarbasHiveMind/LocalHive)    | :question: |  dev  |         |    never    |  
|  [Mycroft Mark1](https://github.com/MycroftAI/enclosure-mark1)    | :question: |  dev  |         |    never    | 
|  [Mycroft Mark2](https://github.com/MycroftAI/hardware-mycroft-mark-II)    | :question: |  dev  |         |    never    |  
|    [NeonGecko](https://neon.ai)      | :question: |  dev  |         |    never    |   
|       [OVOS](https://github.com/OpenVoiceOS)        | :question: |  dev  |         |    never    |    
|     [Picroft](https://github.com/MycroftAI/enclosure-picroft)       | :question: |  dev  |         |    never    |  
| [Plasma Bigscreen](https://plasma-bigscreen.org/)  | :question: |  dev  |         |    never    |  

- `tag` - link to github release / branch / commit
- `version` - link to release/commit of platform repo where this was tested


## Credits
JarbasAl

## Category
**configuration**

## Tags
#configuration
#backend
#privacy
