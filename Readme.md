# Mock Backend Skill

![](./logo.png)

Disable mycroft from phoning home.mycroft.ai


## About

Just install the skill and backend will be disabled

PRIVACY NOTE: you need to setup your own STT, by default it will use google

[kaldi](https://github.com/HelloChatterbox/speech2text/blob/dev/speech2text/engines/kaldi.py) and [deepspeech](https://github.com/HelloChatterbox/speech2text/blob/dev/speech2text/engines/ds.py) are supported

## Configuration

configure backend by editing/creating ~/.mycroft/mock_backend/mock_backend.conf

restarting mycroft is needed after editing this file

see [OpenJarbas/mock-backend](https://github.com/OpenJarbas/mock-backend) for details

```json
{
    "lang": "en-us",
    "stt": {
        "module": "google"
    },
    "backend_port": 6712,
    "ssl": false,
    "ssl_cert": null,
    "ssl_key": null,
    "mail_user": "xxx@gmail.com",
    "mail_password": "xxx",
    "mail_server": "smtp.googlemail.com",
    "mail_port": 465,
    "default_location": {
        "city": {
            "code": "Lawrence",
            "name": "Lawrence",
            "state": {
                "code": "KS",
                "name": "Kansas",
                "country": {
                    "code": "US",
                    "name": "United States"
                }
            }
        },
        "coordinate": {
            "latitude": 38.971669,
            "longitude": -95.23525
        },
        "timezone": {
            "code": "America/Chicago",
            "name": "Central Standard Time",
            "dstOffset": 3600000,
            "offset": -21600000
        }
    },
    "geolocate": false,
    "override_location": false,
    "data_dir": "/home/user/.mycroft/mock_backend",
    "metrics_db": "/home/user/.mycroft/mock_backend/metrics.json",
    "api_version": "v1",
    "email": "xxx@gmail.com"
}
```

## Examples

* "restore mycroft backend"
* "disable mycroft backend"
* "what backend are you using"

## Credits
JarbasAl

## Category
**configuration**

## Tags
#configuration