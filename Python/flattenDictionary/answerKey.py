qaDictionary = {
        'QA1':{
            'q':{
                "Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}},
            'a':{
                "Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e":"1"}},
        'QA2':{
            'q':{
                "Key":{"a":"2","b":"3"}},
            'a':{
                "Key.a":"2","Key.b":"3"}},
        'QA3':{
            'q':{
                "Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}},
            'a':{
                "Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"}},
        'QA4':{
            'q':{
                "":{"a":"1"},"b":"3"},
            'a':{
                "a":"1","b":"3"}},
        'QA5':{
            'q':{
                "a":{"b":{"c":{"d":{"e":{"f":{"":"pramp"}}}}}}},
            'a':{
                "a.b.c.d.e.f":"pramp"}},
        'QA6':{
            'q':{
                "a":"1"},
            'a':{
                "a":"1"}}
        }


