```md
 classDiagram
    AlertPoll <|-- TrafficAlert
    AlertPoll : +double lat
    AlertPoll : +double lon
    AlertPoll : +string timestamp
    AlertPoll : +bool poll_result
    AlertPoll : +fk traffic_alert_id

    TrafficAlert <|-- Localisation
    TrafficAlert <|-- AlertTable
    TrafficAlert : +pk UUID
    TrafficAlert : +double lat
    TrafficAlert : +double lon
    TrafficAlert : +string timestamp
    TrafficAlert : +string report_description
    TrafficAlert : +string localisation_description
    TrafficAlert : +fk localisation_id
    TrafficAlert : +fk alert_id
    
    class Localisation{
        +String city
        +String municipality
        +String postalcode
    }

    class AlertTable{
        +String category
        +String alert_type
        +String alert_subtype
    }
```

[![](https://mermaid.ink/img/pako:eNqFU8FuAiEQ_RXCVf2BTS9N7KFJD03U2yabEWYtERYCw8FY_73solm10HIgMO8Nb-YBZy6sRN5wJjSEsFZw8GDagaXxqtHTp9WavXyvVmzroe-VmKLPhIYtpI17jUzDX6AdCmAgr4YDI2UwEBhXoOyt1cylTecxRF2S6I-McoUdjPFOyfaqdl957uXDCtAqAClb5UzLLaS6C4wk6I5st3tfl8FnN2p4Ub7qSYXl0dnUsMQgvHKVnma6vmv-_6Tk60PCaGuFN_s-EvI8PasHv88ZGMdikysSik6_oyYOSiiXEkuos8kYPb7ejF1ut50V59sr6QHhwfrCqbkFOjmsYSHuZziJ8iU36A0omX7RpNVy-kKDLW_SUoI_trwdLokXnUzCb1KR9bzpQQdccohkN6dB8IZ8xBvp-hGvrMsP3PA3nQ)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNqFU8FuAiEQ_RXCVf2BTS9N7KFJD03U2yabEWYtERYCw8FY_73solm10HIgMO8Nb-YBZy6sRN5wJjSEsFZw8GDagaXxqtHTp9WavXyvVmzroe-VmKLPhIYtpI17jUzDX6AdCmAgr4YDI2UwEBhXoOyt1cylTecxRF2S6I-McoUdjPFOyfaqdl957uXDCtAqAClb5UzLLaS6C4wk6I5st3tfl8FnN2p4Ub7qSYXl0dnUsMQgvHKVnma6vmv-_6Tk60PCaGuFN_s-EvI8PasHv88ZGMdikysSik6_oyYOSiiXEkuos8kYPb7ejF1ut50V59sr6QHhwfrCqbkFOjmsYSHuZziJ8iU36A0omX7RpNVy-kKDLW_SUoI_trwdLokXnUzCb1KR9bzpQQdccohkN6dB8IZ8xBvp-hGvrMsP3PA3nQ)