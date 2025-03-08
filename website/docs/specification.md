# OpenT8-Spezifikation

#### Version 0.2.1

Die Schlüsselwörter "MUSS/MÜSSEN" (*Englisch: "MUST"*), "ERFORDERLICH" (*Englisch: "REQUIRED"*), "EMPFOHLEN" (*Englisch: "RECOMMENDED"*), "SOLLTE" (*Englisch: "SHOULD"*), "SOLLTE NICHT" (*Englisch: "SHOULD NOT"*) und "KANN" *(Englisch: "MAY"*) in diesem Dokument sind so zu interpretieren, wie sie in ihrer englischen Übersetzung in [RFC2119 und RFC8174](https://tools.ietf.org/html/bcp14) spezifiziert sind, und nur dann, wenn sie, wie hier, in Großbuchstaben geschrieben sind.

Dieses Spezifikation ist lizenziert unter der [Apache License, Version 2.0](https://opensource.org/license/apache-2-0/).

## Einführung

OpenT8 definiert ein Standard-Datenformat zur Repräsentation von Stundenplandaten, unabhängig von ihrer Herkunft. Basierend auf dem [JSON-Standard](https://datatracker.ietf.org/doc/html/rfc8259) kann dieses Format mit nahezu jeder Programmiersprache leicht erzeugt und gelesen werden. Mit Hilfe des [OpenT8 Document Schema](https://github.com/openpotato/opent8/tree/main/schemas/v0.2/schema.json) können Dokumente im OpenT8-Format auf ihre syntaktische Korrektheit hin validiert werden.

OpenT8 kann zum Austausch von Stundenplandaten zwischen Diensten oder Anwendungen genutzt werden, als Quelle für die grafische Anzeige von Stundenplänen oder als Antwortformat für API-Anfragen (z.B. für RESTful Web-Services).

## Definitionen

### OpenT8-Dokument

Ein OpenT8-Dokument ist eine in sich geschlossene Ressource, die einen Stundenplan oder Dienstplan definiert und beschreibt. Es MÜSSEN mindestens die Felder `opent8`, `info` und `schedule` enthalten sein. Ein OpenT8-Dokument verwendet die OpenT8-Spezifikation und ist mit ihr konform.

### Personen

Personen (*Englisch: person*) sind Mitglieder (*Englisch: member*) bzw. Teilnehmer (*Englisch: attendee*), die Gruppen, Kursen, Veranstaltungen, Aktivitäten, Aufsichten oder Ereignissen zugeordnet werden. Die Art der Mitgliedschaft bzw. Teilnahme wird dabei jeweils durch ihre Rolle (*Englisch: role*) unterschieden (z.B. Lehrer:in, Erzieher:in, Schüler:in, etc.).

Hier ein Beispiel für die Kursteilnahme eines Lehrers:

``` json
"persons": [
  {
    "id": "Leo",
    "name": {
      "shortName": "Leo",
      "familyName": "Schnitzewitz",
      "familyNamePrefix": "von",
      "middleName": [
        "Leopold"
      ],
      "givenName": "Alexander",
      "title": [
        "Dr."
      ]
    },
    "birthdate": "1969-07-20"
  }
],
"personRoles": [
  {
    "id": "LER",
    "shortName": "LER",
    "longName": "Lehrer:in",
    "code": {
      "codeListRef": {
        "canonicalUri": "urn:opene8:school:codelist:de:personRole",
        "locationUrls": [
          "https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Aschool%3Acodelist%3Ade%3ApersonRole"
        ]
      },
      "keyId": "key",
      "value": "LER"
    }
  }
],
"courses": [
  {
    "id": "DE-1A",
    "shortName": "DE",
    "longName": "Deutsch",
    "subject": {
      "refId": "DE"
    },
    "groups": [
      {
        "refId": "10a"
      }
    ],
    "attendees": [
      {
        "refId": "Leo",
        "role": {
          "refId": "LER"
        }
      }
    ]
  }
]
```

### Gruppen

Gruppen (*Englisch: group*) sind organisatorische Einheiten für Teilnehmer. Sie repräsentieren beispielsweise Klassen, Jahrgänge, Betreuungsgruppen und können durch Gruppentypen kategorisiert werden.

Hier ein Beispiel für zwei Klassen der ersten Jahrgangsstufe:

``` json
"groups": [
  {
    "id": "10a",
    "shortName": "10a",
    "longName": "Klasse 10a",
    "groupType": {
      "refId": "KL"
    }
  },
  {
    "id": "10b",
    "shortName": "10b",
    "longName": "Klasse 10b",
    "groupType": {
      "refId": "KL"
    }
  }
],
"groupTypes": [
  {
    "id": "KL",
    "shortName": "KL",
    "longName": "Klasse",
    "code": {
      "codeListRef": {
	    "canonicalUri": "urn:opene8:school:codelist:de:groupType",
  	    "locationUrls": [
	      "https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Aschool%3Acodelist%3Ade%3AgroupType"
	    ]
      },
      "keyId": "key",
      "value": "KLA"
    }
  }
]
```

### Kurse

Ein Kurs (*Englisch: course*) besteht in der Regel aus einer Serie von Veranstaltungen zu einem bestimmten Fach (*Englisch: subject*). Einem Kurs können Teilnehmer (z.B. Lehrer:innen, Schüler:innen etc.) und Gruppen (z.B. Klassen, Jahrgänge, etc.) zugeordnet werden.

Hier ein Beispiel für einen Kurs:

``` json
"courses": [
  {
    "id": "DE-1A",
    "shortName": "DE",
    "longName": "Deutsch",
    "subject": {
      "refId": "DE"
    },
    "groups": [
      {
        "refId": "1a"
      }
    ],
    "attendees": [
      {
        "refId": "Leo",
        "role": {
          "refId": "LK",
        }
      }
    ]
  },
]
```

### Planelemente

Planelemente (*Englisch: schedule element*) sind die zentralen Objekte, um die sich alles andere gruppiert. Planelemente sind mit Hilfe von zeitlichen Ausdrücken verplant und repräsentieren die sichtbaren Einträge in einem Stundenplan.  

Planelemente sind unterschiedlich ausgeprägt.

#### Veranstaltungen

Veranstaltungen (*Englisch: lesson*) repräsentieren den eigentlichen Unterricht. Eine Veranstaltung MUSS immer mit einem Kurs verknüpft sein. Veranstaltungen umfassen nicht nur ursprünglich geplante Veranstaltungen sondern auch aktuelle Vertretungen (in diesem Fall gibt es eine korrespondierende Fehlstelle mit Verweis auf diese Veranstaltung).

Hier ein Beispiel für die Veranstaltungen eines Musikkurses. Dieser findet jede Woche am Mittwoch und am Donnerstag zu jeweils unterschiedlichen Unterrichtszeiten statt:

``` json
"scheduleElements": [
  {
    "type": "lesson",
    "id": "MU-1A",
    "course": {
      "refId": "MU-1A"
    },
    "rooms": [
      {
        "refId": "200"
      }
    ],
    "temporalExpressions": [
      {
        "type": "weekly",
        "startTimepoint": "2023-09-06T11:00:00",
        "endTimepoint": "2023-09-06T11:45:00"
      },
      {
        "type": "weekly",
        "startTimepoint": "2023-09-07T12:20:00",
        "endTimepoint": "2023-09-07T13:05:00"
      }
    ]
  }
]
```

#### Aufsichten

Aufsichten (*Englisch: supervision*) repräsentieren Zeiten zwischen Unterricht (z.B. in der Pause). Aufsichten umfassen nicht nur ursprünglich geplante Aufsichten sondern auch aktuelle Aufsichtsvertretungen (in diesem Fall gibt es eine korrespondierende Fehlstelle mit Verweis auf diese Aufsicht).

Hier ein Beispiel für eine Pausenhofaufsicht (montags, mittwochs und freitags, zwei Wochen lang):

``` json
"scheduleElements": [
  {
    "type": "supervision",
    "id": "aufsicht-1",
    "notes": "Pausenaufsicht",
    "attendees": [
      {
        "refId": "Leo",
        "role": {
          "refId": "ERZ"
        }
      }
    ],
    "areas": [
      {
        "refId": "Hof"
      }
    ],
    "temporalExpressions": [
      {
        "type": "weekly",
        "startTimepoint": "2023-09-04T08:45:00",
        "endTimepoint": "2023-09-04T09:05:00",
        "validFrom": "2023-09-04T00:00:00",
        "validTo": "2023-09-15T00:00:00"
      },
      {
        "type": "weekly",
        "startTimepoint": "2023-09-06T08:45:00",
        "endTimepoint": "2023-09-06T09:05:00",
        "validFrom": "2023-09-04T00:00:00",
        "validTo": "2023-09-15T00:00:00"
      },
      {
        "type": "weekly",
        "startTimepoint": "2023-09-08T08:45:00",
        "endTimepoint": "2023-09-08T09:05:00",
        "validFrom": "2023-09-04T00:00:00",
        "validTo": "2023-09-15T00:00:00"
      }
    ]
  }
]
```

#### Aktivitäten

Aktivitäten (*Englisch: activity*) repräsentieren Dienstzeiten, die keine Lehrveranstaltungen sind (z.B. Bereitschaftsdienst, Hortaufsicht, etc.).

Hier ein Beispiel für eine Hortaufsicht:

``` json
"scheduleElements": [
  {
    "type": "activity",
    "id": "ho-1",
    "shortName": "HoAmAbend",
    "longName": "Hortaufsicht am Abend",
	"activityType": {
      "refId": "HA"
    },
    "attendees": [
      {
        "refId": "Eli",
        "role": {
          "refId": "ERZ"
        }
      }
    ],
    "rooms": [
      {
        "refId": "200"
      }
    ],
    "temporalExpressions": [
      {
        "type": "onetime",
        "startTimepoint": "2023-09-01T16:00:00",
        "endTimepoint": "2023-09-01T18:00:00"
      }
    ]
  }
],
"activityTypes": [
  {
    "id": "HA",
    "shortName": "HA",
    "longName": "Hortaufsicht"
  }
]
```

#### Ereignisse

Ereignisse (*Englisch: event*) sind Termine, die nicht durch Veranstaltungen, Aktivitäten oder Aufsichten repräsentiert werden können (z.B. Meetings, Prüfungen, etc.).

Hier ein Beispiel für ein Meeting:

``` json
"scheduleElements": [
  {
    "type": "event",
    "id": "meet-1",
    "shortName": "Meeting",
    "longName": "Abstimmung zur Einschulung",
	"eventType": {
      "refId": "KONFI"
    },
    "attendees": [
      {
        "refId": "Max",
        "role": {
          "refId": "LEH"
        }
      },
      {
        "refId": "Eli",
        "role": {
          "refId": "LEH"
        }
      }
    ],
    "rooms": [
      {
        "refId": "LeZi"
      }
    ],
    "temporalExpressions": [
      {
        "type": "onetime",
        "startTimepoint": "2023-09-01T08:00:00",
        "endTimepoint": "2023-09-01T10:00:00"
      }
    ]
  }
],
"eventTypes": [
  {
    "id": "KONFI",
    "shortName": "KONFI",
    "longName": "Konferenz"
  }
]
```

#### Ferien und Feiertage

Ferien bzw. Feiertage (*Englisch: holiday*) repräsentieren Tage, an denen kein Unterricht stattfindet.

Hier die Weihnachtsferien 2023/2024 als Beispiel:

``` json
"scheduleElements": [
  {
    "type": "holiday",
    "id": "WeiFe",
    "shortName": "WeiFe",
    "longName": "Weihnachtsferien",
    "holidayType": "school",
    "temporalExpressions": [
      {
        "type": "onetime",
        "startTimepoint": "2023-12-23T00:00:00",
        "endTimepoint": "2024-01-05T00:00:00"
      }
    ]
  }
]
```

#### Mitteilungen

Mitteilungen (*Englisch: announcement*) erlauben die Anzeige von zusätzlichen Informationen direkt im Stundenplan.

Hier ein Beispiel für einen Hinweis zum Feueralarm:

``` json
"scheduleElements": [
  {
    "type": "announcement",
    "id": "alarm-1",
    "shortDescription": "alarm",
    "longDescription": "Feueralarmübung",
    "notes": "Feueralarmübung am Morgen",
    "color": "#E55604",
    "temporalExpressions": [
      {
        "type": "onetime",
        "startTimepoint": "2023-12-23T08:00:00",
        "endTimepoint": "2024-01-05T08:25:00"
      }
    ]
  }
]
```

#### Fehlstellen

Fehlstellen (*Englisch: gap*) repräsentieren Veranstaltungen, Aufsichten oder Aktivitäten, die nicht wie geplant stattfinden können. Eine Fehlstelle definiert neben der Zeit die Gründe (*Englisch: reason*) für die Planänderung (z.B. Lehrer fehlt/ist freigestellt oder Raum ist nicht verfügbar) und die Auflösung (*Englisch: resolution*). Die Auflösung kann entweder eine Vertretung bzw. ein Ersatz (*Englisch: substitution*) oder der Ausfall (*Englisch: cancellation*) sein.

Hier ein Beispiel für einen Lehrerausfall. Der Unterricht wird durch einen Erzieher vertreten:

``` json
"scheduleElements": [
  {
    "type": "gap",
    "id": "G-1",
    "notes": "Das ist eine Fehlstelle",
    "appliesTo": {
      "type": "lesson",
      "refId": "DE-1A"
    },
    "reasons": [
      {
        "type": "absence",
        "notes": "Lehrer ist krank",
        "appliesTo": {
          "type": "person",
          "refId": "Max"
        }
      }
    ],
    "resolutions": [
      {
        "type": "substitution",
        "notes": "Der Erzieher springt ein",
        "realisedBy": {
          "type": "lesson",
          "refId": "V-1"
        }
      }
    ],
    "temporalExpressions": [
      {
        "type": "onetime",
        "startTimepoint": "2023-09-04T08:00:00",
        "endTimepoint": "2023-09-04T08:45:00"
      }
    ]
  },
  {
    "type": "lesson",
    "id": "V-1",
    "notes": "Das ist eine Vertretung",
    "course": {
      "refId": "DE-1A"
    },
    "attendees": [
      {
        "refId": "Leo",
        "role": {
          "refId": "EZ"
        }
      }
    ],
    "rooms": [
      {
        "refId": "102"
      }
    ],
    "temporalExpressions": [
      {
        "type": "onetime",
        "startTimepoint": "2023-09-04T08:00:00",
        "endTimepoint": "2023-09-04T08:45:00"
      }
    ]
  }
]
```

### Räume, Gebäude, Campus und Aufsichtsbereiche

Planelemente können mit Standorten verknüpft werden. Für Veranstaltungen, Aktivitäten und Ereignisse sind dies Räume (*Englisch: room*), für Aufsichten sind dies Aufsichtsbereiche (*Englisch: supervision area*). Räume können für ein Gebäude (*Englisch: building*) zusammengefasst, Gebäude wiederum für einen Campus (*Englisch: campus*) zusammengefasst werden. Auch Aufsichtsbereiche können für einen Campus zusammengefasst werden.

Hier ein Beispiel für zwei Räume mit Verweis auf das gleiche Gebäude:

``` json
"rooms": [
  {
    "id": "100",
    "shortName": "100",
    "longName": "Raum 100",
    "building": {
      "refId": "HG"
    }
  },
  {
    "id": "101",
    "shortName": "101",
    "longName": "Raum 101",
    "building": {
      "refId": "HG"
    }
  }
]
```

### Zeitliche Ausdrücke

Zeitliche Ausdrücke (*Englisch: temporal expression*) erlauben eine flexible zeitliche Planung von Planelementen. 

Die folgenden zeitlichen Ausdrücke werden unterstützt:

#### Einmalig 

Einmalige (*Englisch: one time*) Ausdrücke repräsentieren einen einmaligen Termin, definiert durch ein Startzeitpunkt und einem Endzeitpunkt. Ein einmaliger Termin kann auch mehrtägig sein (z.B. Sommerferien).

Hier ein Beispiel für einen einmaligen Termin.

``` json
"temporalExpressions": [
  {
    "type": "onetime",
    "startTimepoint": "2023-09-04T08:00:00",
    "endTimepoint": "2023-09-04T08:45:00"
  }
]
```

#### Wöchentlich

Wöchentlich (*Englisch: weekly*) Ausdrücke repräsentieren sich wöchentlich wiederholendende Termine, beginnend mit einem konkretem Termin, definiert durch ein Startzeitpunkt und einem Endzeitpunkt. Standardmäßig findet dieser Termin in jeder Woche innerhalb des Gültigkeitszeitraum des Stundenplans statt. Es können jedoch optional einzelne Wochen deaktiviert werden, so dass ein Wochenmuster entsteht (z.B. 14-tägig, jede dritte Woche, etc.).

Hier ein Beispiel für einen wöchentlichen Termin, der jedoch nur in bestimmten Kalenderwochen stattfindet:

``` json
"temporalExpressions": [
  {
    "type": "weekly",
    "startTimepoint": "2023-09-08T11:00:00",
    "endTimepoint": "2023-09-08T11:45:00",
    "weeks": [
      "2023:36,38,40,42,44,46,48,50",
      "2024:1-4"
    ]
  }
]
```

#### Kombination

Zeitliche Ausdrücke können miteinander kombiniert und sowohl positiv (findet statt) als auch negativ (findet nicht statt) definiert werden. Die Kombination aus positiven und negativen zeitlichen Ausdrücken erlaubt die Repräsentation von zeitlichen Ausnahmen (z.B. Immer Montags von 8:00 bis 8:45, nur nicht im Juli und im August).

Hier ein Beispiel für einen zeitlichen Ausdruck, bestehend aus einem wöchentlichen Termin, der jedoch an einem bestimmten Tag nicht stattfindet:

``` json
"temporalExpressions": [
  {
    "type": "weekly",
    "startTimepoint": "2023-09-08T11:00:00",
    "endTimepoint": "2023-09-08T11:45:00",
    "operation": "include"
  },
  {
    "type": "onetime",
    "startTimepoint": "2023-09-22:00:00",
    "endTimepoint": "2023-09-22T00:00:00",
    "operation": "exclude"
  }
]
```

### Zeitrahmen

Planelemente werden u.a. durch konkrete Uhrzeiten definiert. Ein Zeitrahmen (*Englisch: time frame*) erlaubt eine Abbildung der Planelemente auf ein Stundenraster (z.B. 1. Stunde, 2. Stunde, Pause, etc.), das eine zeitlich abstrahierte Darstellung des Stundenplans ermöglicht. 

Hier ein Beispiel für einen Zeitrahmen in einer Grundschule (Jahrgangsstufe 1):

``` json
"timeFrames": [
  {
    "id": "default",
    "shortName": "Unterricht",
    "longName": "Unterrichtsraster",
    "scopeOfWeek": [
      "mon",
      "tue",
      "wed",
      "thu",
      "fri"
    ],
    "timeSlots": [
      {
        "shortLabel": "1",
        "longLabel": "1. Stunde",
        "startTime": "08:00:00",
        "endTime": "08:45:00"
      },
      {
        "shortLabel": "2",
        "longLabel": "2. Stunde",
        "startTime": "09:05:00",
        "endTime": "09:50:00"
      },
      {
        "shortLabel": "3",
        "longLabel": "3. Stunde",
        "startTime": "10:10:00",
        "endTime": "10:55:00"
      },
      {
        "shortLabel": "4",
        "longLabel": "4. Stunde",
        "startTime": "11:00:00",
        "endTime": "11:45:00"
      },
      {
        "shortLabel": "5",
        "longLabel": "5. Stunde",
        "startTime": "12:20:00",
        "endTime": "13:05:00"
      }
    ]
  }
]
```

### Standardisierte Codes

Standardisierte Codes erlauben die eindeutige Identifikation und Klassifikation von Daten. OpenT8 unterstützt [OpenCodeList](https://openpotato.github.io/opencodelist/de/), einem generischen Standard-Datenformat zur Repräsentation von Code-Listen bzw. Schlüsselverzeichnissen. 

Die folgenden Objekte besitzen jeweils ein (zum Teil erforderliches) Code-Attribut, dass einen Verweis auf eine Code-Liste im OpenCodeList-Format darstellt. 

+ `absenceType`-Objekt (Abwesenheitstyp)
+ `activityType`-Objekt (Aktivitätstyp)
+ `courseType`-Objekt (Kurstyp)
+ `eventType`-Objekt (Eriegbistyp)
+ `exemptionType`-Objekt (Freistellungsformat)
+ `gender`-Objekt (Geschlecht)
+ `groupType`-Objekt (Gruppentyp)
+ `personRole`-Objekt (Personenrolle)
+ `subject`-Objekt (Fach)
+ `supervisionType`-Objekt (Aufichtstyp)
+ `teachingFormat`-Objekt (Unterrichtsformat)

In einigen Fällen wird eine Standard-Code-Liste spezifiziert. Alle Standard-Code-Listen sind via [CodeListHub](https://www.codelisthub.org/de/) verfügbar und abrufbar.

Hier ein Beispiel für ein Gruppentyp mit einem standardisierten Code:

``` json
"groupTypes": [
  {
    "id": "KL",
    "shortName": "KL",
    "longName": "Klasse",
    "code": {
      "codeListRef": {
	    "canonicalUri": "urn:opene8:school:codelist:de:groupType",
  	    "locationUrls": [
	      "https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Aschool%3Acodelist%3Ade%3AgroupType"
	    ]
      },
      "keyId": "key",
      "value": "KLA"
    }
  }
]
```

### Externe Identifikatoren

Externe Identifikatoren erlauben das Verknüpfen von IDs aus Fremdsystemen mit Entitäten im OpenT8-Format. Unterstützt werden folgende Objekte:

+ `building`-Objekt (Gebäude)
+ `campus`-Objekt (Campus)
+ `course`-Objekt (Kurs)
+ `group`-Objekt (Gruppe)
+ `person`-Objekt (Person)
+ `room`-Objekt (Raum)
+ `subject`-Objekt (Fach)
+ `supervisionArea`-Objekt (Aufsichtsbereich)

Hier ein Beispiel für ein Fach mit zwei externen Identifikatoren:

``` json
"subjects": [
  {
    "id": "DE",
    "shortName": "DE",
    "longName": "Deutsch",
    "externalIds": [
      {
	    "canonicalUri": "urn:myTimeTableApp1",
	    "globallyUnique": true,
  	    "value": "eb002793-570e-45c7-af17-423831240b83"
	  },
	  {
	    "canonicalUri": "urn:myTimeTableApp2",
	    "globallyUnique": false,
  	    "value": "42"
	  }
    ]
  }
]
```

## Spezifikation

### Versionierung

Die OpenT8-Spezifikation wird nach dem Schema `major.minor.patch` versioniert. Der Major-Minor-Teil der Versionsnummer (z.B. `0.2`) MUSS den Funktionssatz der Spezifikation bezeichnen. Die Patch-Versionen betreffen Fehler in diesem Dokument oder stellen Klarstellungen zu diesem Dokument bereit, nicht zum Funktionsumfang. Werkzeuge, die OpenT8 in der Version `0.2` unterstützen, MÜSSEN mit allen `0.2.*` Versionen von OpenT8 kompatibel sein. Die Patch-Version SOLLTE von den Werkzeugen NICHT berücksichtigt werden, so dass zum Beispiel kein Unterschied zwischen `0.2.1` und `0.2.2` gemacht wird.

Ein OpenT8-Dokument enthält stets ein obligatorisches Feld `opent8`, das die verwendete Version der OpenT8-Spezifikation angibt.

### Format

Ein OpenT8-Dokument, das mit der OpenT8-Spezifikation konform ist, ist selbst ein JSON-Objekt, das im JSON-Format dargestellt werden kann.

Bei allen Feldnamen in der Spezifikation wird zwischen Groß- und Kleinschreibung unterschieden. 

Das Schema sieht zwei Arten von Feldern vor: Fest definierte Felder, die einen deklarierten Namen haben, und freie Felder, deren Namen aber einem bestimmten Muster (*Englisch: pattern*) entsprechen MÜSSEN. Zusatzfelder MÜSSEN innerhalb des enthaltenen JSON-Objekts eindeutige Namen haben.

#### JSON Schema

[JSON Schema](https://json-schema.org/) ist eine Spezifikation zur Definition von JSON-Datenstrukturen. Ein JSON-Schema wird selbst deklarativ durch [JSON](https://www.json.org/) ausgedrückt. Das [OpenT8 Document Schema](https://github.com/openpotato/opent8/tree/main/schemas/v0.2/schema.json) ist ein JSON-Schema für OpenT8-Dokumente.

#### Datums- und Zeitangaben

Die Formatierung der Datums- und Zeitangaben in OpenT8 sind, wie von [JSON Schema](https://json-schema.org/understanding-json-schema/reference/string.html#dates-and-times) vorgegeben, durch [RFC 3339, Abschnitt 5.6](https://tools.ietf.org/html/rfc3339#section-5.6) spezifiziert.

Beispiele:

+ **`date-time`** : Datum und Zeit zusammen, z.B. `2023-11-13T20:20:39` oder `2023-11-13T20:20:39+00:00`.
+ **`time`** : Nur Uhrzeit, z.B. `20:20:39` oder `20:20:39+00:00`.
+ **`date`** : Nur Datum, z.B. `2023-11-13`.

#### Kalenderwochen

Kalenderwochen werden durch ein JSON-Array mit formatierten Strings repräsentiert. Jeder formatierte String definiert die Menge der gewünschten Kalenderwochen für genau ein benanntes Jahr. Der Syntax lautet:

```
<Jahr>:(<Kalenderwoche>|<Kalenderwoche>-<Kalenderwoche>)[,(<Kalenderwoche>|<Kalenderwoche>-<Kalenderwoche>)]
```

Eine Kalenderwoche ist nach ISO 8601 wie folgt definiert:

+ Kalenderwochen haben 7 Tage, beginnen an einem Montag und werden über das Jahr fortlaufend nummeriert.
+ Die Kalenderwoche 1 eines Jahres ist diejenige, die den ersten Donnerstag enthält.
+ Je nach Jahr kann es entweder 52 oder 53 Kalenderwochen geben.

Statt einzelner Kalenderwochen (z.B. `10`) können auch Kalenderwochenbereiche (z.B. `10-12`) definiert werden.

Ein Beispiel, bei dem für das Jahr 2023 die Kalenderwochen 36, 38, 40, 42, 44, 46, 48 und 50, sowie für das Jahr 2024 die ersten 4 Wochen markiert sind:

``` json
"weeks": [
  "2023:36,38,40,42,44,46,48,50",
  "2024:1-4"
]
```

#### Farbwerte

Die Formatierung der Farbwerte in OpenT8 orientiert sich am [hexadezimale Farbsystem](https://www.w3schools.com/html/html_colors_hex.asp), so wie es auch im HTML-Standard definiert ist.

Eine hexadezimale Farbe wird angegeben mit: #RRGGBB, wobei die hexadezimalen Ganzzahlen RR (Rot), GG (Grün) und BB (Blau) die Komponenten der Farbe angeben.

Beispiele:

+ `#ff0000` ist rot
+ `#00ff00` ist grün
+ `#0000ff` ist blau
+ `#ff8000` ist orange

### Schema

#### OpenT8-Objekt

Dies ist das Wurzelobjekt eines OpenT8-Dokuments und enthält folgende Felder:

**`opent8`**

:   Definiert die Versionsnummer der OpenT8-Spezifikation. **Dieses Feld ist ERFORDERLICH**.

**`info`**

:   Metadaten zum Stundenplan. **Dieses Objekt ist ERFORDERLICH**.

**`absenceTypes`**

:   Eine Liste von Abwesenheitstypen. Es MUSS ein JSON-Array mit `absenceType`-Objekten sein. 

**`activityTypes`**

:   Eine Liste von Aktivitätstypen. Es MUSS ein JSON-Array mit `activityType`-Objekten sein. 

**`buildings`**

:   Eine Liste von Gebäuden. Es MUSS ein JSON-Array mit `building`-Objekten sein. 

**`campuses`** 

:   Eine Liste von Campus. Es MUSS ein JSON-Array mit `campus`-Objekten sein. 

**`courses`** 

:   Eine Liste von Kursen. Es MUSS ein JSON-Array mit `course`-Objekten sein. 

**`courseTypes`**

:   Eine Liste von Kurstypen. Es MUSS ein JSON-Array mit `courseType`-Objekten sein. 

**`eventTypes`** 

:   Eine Liste von Ereignistypen. Es MUSS ein JSON-Array mit `eventType`-Objekten sein. 

**`exemptionTypes`**

:   Eine Liste von Freistellungstypen. Es MUSS ein JSON-Array mit `exemptionType`-Objekten sein. 

**`genders`** 

:   Eine Liste von Angaben zum Personengeschlecht. Es MUSS ein JSON-Array mit `gender`-Objekten sein. 

**`groups`**

:   Eine Liste von Gruppen. Es MUSS ein JSON-Array mit `group`-Objekten sein. 

**`groupTypes`**

:   Eine Liste von Gruppentypen. Es MUSS ein JSON-Array mit `groupType`-Objekten sein. 

**`persons`**

:   Eine Liste von Personen. Es MUSS ein JSON-Array mit `person`-Objekten sein. 

**`personRoles`**

:   Eine Liste von Personenrollen. Es MUSS ein JSON-Array mit `personRole`-Objekten sein. 

**`rooms`**

:   Eine Liste von Räumen. Es MUSS ein JSON-Array mit `room`-Objekten sein.  

**`subjects`** 

:   Eine Liste von Fächern. Es MUSS ein JSON-Array mit `subject`-Objekten sein.  

**`supervisionAreas`** 

:   Eine Liste von Aufsichtsbereichen. Es MUSS ein JSON-Array mit `supervisionArea`-Objekten sein. 

**`supervisionTypes`** 

:   Eine Liste von Aufsichtstypen. Es MUSS ein JSON-Array mit `supervisionType`-Objekten sein. 

**`teachingFormats`**

:   Eine Liste von Unterrichtsformaten. Es MUSS ein JSON-Array mit `teachingFormat`-Objekten sein. 

**`timeFrames`** 

:   Eine Liste von Zeitrahmen. Es MUSS ein JSON-Array mit `timeFrame`-Objekten sein. 

**`schedule`** 

:   Die eigentliche zeitliche Verplanung. **Dieses Objekt ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### absence-Objekt

Das `absence`-Objekt definiert eine Abwesenheit:

**`type`** 

:   MUSS den Wert `absence` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Abwesenheit. **Dieses Feld ist ERFORDERLICH**.

**`notes`** 

:   Bemerkungen zur Abwesenheit.

**`absenceType.refId`** 

:   Typ des Abwesenheit. Dies MUSS ein Verweis auf die `id` eines `absenceType`-Objekts sein. 

**`appliesTo`** 

:   Eine Person, eine Gruppe oder ein Raum, für welche(n) die Abwesenheit gilt. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
    
        Mögliche Werte sind:
    
        Wert     | Beschreibung
        -------- | ------------
        `person` | Eine Person ist abwesend.
        `group`  | Eine Gruppe ist abwesend.
        `room`   | Der Raum steht nicht zur Verfügung.
        
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `person`-Objekts, eines vorhandenen `group`-Objekts oder eines vorhandenen `room`-Objekts sein, jeweils in Abhängigkeit vom Wert in Feld `type`. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### absenceType-Objekt

Das `absenceType`-Objekt repräsentiert einen Abwesenheitstyp, mit dem Abwesenheiten kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Abwesenheitstyp. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Es wird keine Code-Liste empfohlen.

**`shortName`** 

:   Kürzel des Abwesenheitstyp. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Abwesenheitstyp. 

**`description`** 

:   Eine kurze Beschreibung des Abwesenheitstyp.

Dieses Objekt KANN erweitert werden.

#### activity-Objekt

Das `activity`-Objekt definiert eine Aktivität:

**`type`** 

:   MUSS den Wert `activity` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Aktivität. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel der Aktivität. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name der Aktivität. 

**`description`** 

:   Eine kurze Beschreibung der Aktivität. 

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Mitteilung.

**`activityType.refId`** 

:   Typ der Aktivität. Dies MUSS ein Verweis auf die `id` eines `activityType`-Objekts sein. 

**`attendees`** 

:   Eine Liste von Teilnehmern und deren Rollen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `person`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role.refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `personRole`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`rooms`** 

:   Eine Liste von genutzten Räumen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `room`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### activityType-Objekt

Das `activityType`-Objekt repräsentiert einen Aktivitätstyp, mit dem Aktivitäten kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Aktivitätstyp. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Es wird keine Code-Liste empfohlen.

**`shortName`** 

:   Kürzel des Aktivitätstyp. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Aktivitätstyp. 

**`description`** 

:   Eine kurze Beschreibung des Aktivitätstyp.

Dieses Objekt KANN erweitert werden.

#### announcement-Objekt

Das `announcement`-Objekt repräsentiert eine freie Mitteilung im Stundenplan:

**`type`** 

:   MUSS den Wert `announcement` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Mitteilung. **Dieses Feld ist ERFORDERLICH**.

**`shortDescription`** 

:   Kurzbeschreibung der Mitteilung. **Dieses Feld ist ERFORDERLICH**.

**`longDescription`** 

:   Ausführlicher Inhalt der Mitteilung. 

**`notes`** 

:   Bemerkungen zur Mitteilung.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Mitteilung.

**`priority`** 

:   Die Priorität der Mitteilung. 

    Folgende Werte sind definiert:

    Wert        | Beschreibung
    ----------- | ------------
    `important` | Wichtig
    `alarm`     | Alarm

**`appliesTo`** 

:   Eine Liste von Gruppen oder Personen, für welche die Mitteilung gilt. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
    
        Mögliche Werte sind:
    
        Wert     | Beschreibung
        -------- | ------------
        `person` | Eine Person
        `group`  | Eine Gruppe
        
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `person`-Objekts, eines vorhandenen `group`-Objekts oder eines vorhandenen `room`-Objekts sein, jeweils in Abhängigkeit vom Wert in Feld `type`. **Dieses Feld ist ERFORDERLICH**.

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### building-Objekt

Das `building`-Objekt repräsentiert ein Gebäude, in dem sich Räume befinden:

**`id`** 

:   Eindeutige Identifikation des Gebäudes. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel des Gebäudes. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Gebäudes. 

**`description`** 

:   Eine kurze Beschreibung des Gebäudes.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für das Gebäude.

**`campus.refId`** 

:   Der Campus, auf dem sich das Gebäude befindet. Dies MUSS ein Verweis auf die `id` eines `campus`-Objekts sein. 

**`externalIds`** 

:   Eine optionale List von externen Identifikatoren. Es MUSS ein JSON-Array mit `externalId`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### campus-Objekt

Das `campus`-Objekt repräsentiert einen Campus, auf dem sich Gebäude und/oder Aufsichtsbereiche befinden:

**`id`** 

:   Eindeutige Identifikation des Campus. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel des Campus. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Campus. 

**`description`** 

:   Eine kurze Beschreibung des Campus.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Campus.

**`externalIds`** 

:   Eine optionale List von externen Identifikatoren. Es MUSS ein JSON-Array mit `externalId`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### cancellation-Objekt

Das `cancellation`-Objekt definiert einen Unterrichtsausfall:

**`type`** 

:   MUSS den Wert `cancellation` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation des Unterrichtsausfalls. **Dieses Feld ist ERFORDERLICH**.

**`notes`** 

:   Bemerkungen zum Unterrichtsausfall.

**`behaviour`** 

:   Mögliches Verhalten

    + **`leaveRoom`** : Den Unterrichtsraum verlassen
    + **`stayInRoom`** : Im Unterrichtsraum bleiben

Dieses Objekt KANN erweitert werden.

#### course-Objekt

Das `course`-Objekt repräsentiert einen Kurs, in dem sich Gruppen und/oder Teilnehmer treffen und der Veranstaltungen zugeordnet werden kann:

**`id`** 

:   Eindeutige Identifikation des Kurses. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel des Kurses. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Kurses. 

**`description`** 

:   Eine kurze Beschreibung des Kurses.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Kurs.

**`subject.refId`** 

:   Das zugeordnete Fach. Dies MUSS ein Verweis auf die `id` eines vorhandenen `subject`-Objekts sein. 

**`courseNo`** 

:   Eine Kursnummer.

**`courseType.idRef`** 

:   Typ der Kurses. Dies MUSS ein Verweis auf die `id` eines `courseType`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`courseUrl`** 

:   Eine URL zu einer externen Website mit zusätzlichen Infos zu diesem  Kurs.

**`groups`** 

:   Eine Liste von teilnehmenden Gruppen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `group`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`attendees`** 

:   Eine Liste von Teilnehmern und deren Rollen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `person`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role.refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `personRole`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`externalIds`** 

:   Eine optionale List von externen Identifikatoren. Es MUSS ein JSON-Array mit `externalId`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### courseType-Objekt

Das `courseType`-Objekt repräsentiert einen Kurstyp, mit dem Gruppen kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Kurstyps. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. **Dieses Feld ist ERFORDERLICH**. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Standardmäßig wird folgende Code-Liste EMPFOHLEN:
    
    CanonicalURI                               | URL
    ------------------------------------------ | ---
    `urn:opene8:school:codelist:de:courseType` | [Link](https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Aschool%3Acodelist%3Ade%3AcourseType)

**`shortName`** 

:   Kürzel des Gruppentyps. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Kurstyps. 

**`description`** 

:   Eine kurze Beschreibung des Kurstyps.

Dieses Objekt KANN erweitert werden.

#### event-Objekt

Das `event`-Objekt repräsentiert ein Termin, dass sich nicht durch eine Veranstaltung ausdrücken lässt (z.B. eine Prüfung oder ein Meeting):

**`type`** 

:   MUSS den Wert `event` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation des Termins. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel des Termins. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Termins. 

**`description`** 

:   Eine kurze Beschreibung des Termins.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Termin.

**`eventType.refId`** 

:   Typ des Ereignisses. Dies MUSS ein Verweis auf die `id` eines `eventType`-Objekts sein. 

**`groups`** 

:   Eine Liste von teilnehmenden Gruppen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `group`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`attendees`** 

:   Eine Liste von Teilnehmern und deren Rollen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `person`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role.refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `personRole`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`rooms`** 

:   Eine Liste von genutzten Räumen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `room`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### eventType-Objekt

Das `eventType`-Objekt repräsentiert einen Ereignistyp, mit dem Ereignisse kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Ereignistyps. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Es wird keine Code-Liste empfohlen.

**`shortName`** 

:   Kürzel des Ereignistyps. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Ereignistyps. 

**`description`** 

:   Eine kurze Beschreibung des Ereignistyps.

Dieses Objekt KANN erweitert werden.

#### exemption-Objekt

Das `exemption`-Objekt definiert eine Freistellung:

**`type`** 

:   MUSS den Wert `exemption` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Freistellung. **Dieses Feld ist ERFORDERLICH**.

**`notes`** 

:   Bemerkungen zur Freistellung.

**`exemptionType.refId`** 

:   Typ des Freistellung. Dies MUSS ein Verweis auf die `id` eines `exemptionType`-Objekts sein. 

**`appliesTo`** 

:   Eine Person, für welche(n) die Freistellung gilt. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
    
        Mögliche Werte sind:
    
        Wert     | Beschreibung
        -------- | ------------
        `person` | Eine Person ist freigestellt.
        
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `person`-Objekts sein, jeweils in Abhängigkeit vom Wert in Feld `type`. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### exemptionType-Objekt

Das `exemptionType`-Objekt repräsentiert einen Freistellungstyp, mit dem Ereignisse kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Freistellungstyp. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Es wird keine Code-Liste empfohlen.

**`shortName`** 

:   Kürzel des Freistellungstyp. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Freistellungstyp. 

**`description`** 

:   Eine kurze Beschreibung des Freistellungstyp.

Dieses Objekt KANN erweitert werden.

#### externalCode-Objekt

Das `externalCode`-Objekt definiert einen Code aus einer externen Code-Liste im OpenCodeList-Format:

**`codeListRef`** 

:   Ein Objekt, das auf eine externe Code-Liste verweist. **Dieses Feld ist ERFORDERLICH**.

**`codeListRef.canonicalUri`** 

:   Ein JSON-String im Format `uri`. Diese URI identifiziert alle Versionen (zusammen) der referenzierten Code-Liste eindeutig. **Dieses Feld ist ERFORDERLICH**.

**`codeListRef.canonicalVersionUri`** 

:   Ein JSON-String im Format `uri`. Diese URI identifiziert eine bestimmte Version der referenzierten Code-Liste.

**`codeListRef.locationUrls`** 

:   Ein JSON-Array mit JSON-String-Werten im Format `uri`. Diese URIs sind vorgeschlagene Abruforte für die referenzierte Code-Liste, im OpenCodeList-Format.

**`keyId`** 

:   Ein JSON-String mit einer ID, die auf ein key-Objekt in der unter codeListRef definierten externen Code-Liste verweist. **Dieses Feld ist ERFORDERLICH**.

**`value`** 

:   Ein Code aus der externen Code-Liste. **Dieses Feld ist ERFORDERLICH**.

#### externalId-Objekt

Das `externalId`-Objekt definiert einen externen Identifikator:

**`canonicalUri`** 

:   Ein JSON-String im Format `uri`. Diese URI legt den Namensraum des externen Identifikator fest bzw. gibt Auskunft darüberm, zu wem der Identifikator gehört. **Dieses Feld ist ERFORDERLICH**.

**`globallyUnique`** 

:   Ein JSON-Boolean, der angibt, ob der Identifikator eine globale Eindeutigkeit. **Dieses Feld ist ERFORDERLICH**.

**`value`** 

:   Der eigentliche Identifikator-Wert. **Dieses Feld ist ERFORDERLICH**.

#### gap-Objekt

Das `gap`-Objekt repräsentiert eine Fehlstelle im Stundenplan:

**`type`** 

:   MUSS den Wert `gap` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Fehlstelle. **Dieses Feld ist ERFORDERLICH**.

**`notes`** 

:   Bemerkungen zur Fehlstelle.

**`appliesTo`** 

:   Eine Aktivität, eine Unterrichtseinheit oder eine Aufsicht, für welche(n) die Fehlstelle gilt. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
    
        Mögliche Werte sind:
    
        Wert          | Beschreibung
        ------------- | ------------
        `activity`    | Fehlstelle für eine Aktivität
        `lesson`      | Fehlstelle für eine Unterrichtseinheit
        `supervision` | Fehlstelle für eine Aufsicht
        
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `activity`-Objekts, eines vorhandenen `lesson`-Objekts oder eines vorhandenen `supervision`-Objekts sein, jeweils in Abhängigkeit vom Wert in Feld `type`. **Dieses Feld ist ERFORDERLICH**.

**`reasons`** 

:   Eine Liste von Gründen. Es MUSS ein JSON-Array mit `absence`-Objekten und/oder `exemption`-Objekten sein. 

**`resolutions`** 

:   Eine Liste von Auflösungen. Es MUSS ein JSON-Array mit `substitution`-Objekten und/oder `cancellation`-Objekten sein. 

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### gender-Objekt

Das `gender`-Objekt definiert das Geschlecht einer Person:

**`id`** 

:   Eindeutige Identifikation des Geschlechts. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. **Dieses Feld ist ERFORDERLICH**. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Standardmäßig wird folgende Code-Liste EMPFOHLEN:
    
    CanonicalURI                         | URL
    ------------------------------------ | ---
    `urn:opene8:core:codelist:de:gender` | [Link](https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Acore%3Acodelist%3Ade%3Agender)

**`shortName`** 

:   Kürzel des Geschlechts. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Geschlechts. 

**`description`** 

:   Eine kurze Beschreibung des Geschlechts.

Dieses Objekt KANN erweitert werden.

#### group-Objekt

Das `group`-Objekt repräsentiert eine Gruppe, der man Teilnehmer zuordnen kann:

**`id`** 

:   Eindeutige Identifikation der Gruppe. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel der Gruppe. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name der Gruppe. 

**`description`** 

:   Eine kurze Beschreibung der Gruppe.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Gruppe.
    
**`groupType.idRef`** 

:   Typ der Gruppe. Dies MUSS ein Verweis auf die `id` eines `groupType`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`members`** 

:   Eine Liste von Mitgliedern und deren Rollen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `person`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role.refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `personRole`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`timeFrame`** 

:   Der Zeitrahmen des Teilnehmers. Dies MUSS ein `reference`-Objekt, das auf ein `timeFrame`-Objekt verweist, sein. Diese Angabe macht nur Sinn, wenn sie vom Standardzeitrahmen des Stundenplans abweicht.

**`externalIds`** 

:   Eine optionale List von externen Identifikatoren. Es MUSS ein JSON-Array mit `externalId`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### groupType-Objekt

Das `groupType`-Objekt repräsentiert einen Gruppentyp, mit dem Gruppen kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Gruppentyps. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. **Dieses Feld ist ERFORDERLICH**. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Standardmäßig wird folgende Code-Liste EMPFOHLEN:
    
    CanonicalURI                              | URL
    ----------------------------------------- | ---
    `urn:opene8:school:codelist:de:groupType` | [Link](https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Aschool%3Acodelist%3Ade%3AgroupTyp)

**`shortName`** 

:   Kürzel des Gruppentyps. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Gruppentyps. 

**`description`** 

:   Eine kurze Beschreibung des Gruppentyps.

Dieses Objekt KANN erweitert werden.

#### holiday-Objekt

Das `holiday`-Objekt repräsentiert schulfreie Zeit (Feiertage oder Schulferien):

**`type`** 

:   MUSS den Wert `holiday` haben. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel der schulfreie Zeit. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name der schulfreie Zeit 

**`description`** 

:   Eine kurze Beschreibung der schulfreie Zeit.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die schulfreie Zeit.

**`holidayType`** 

:   Die Typisierung des Termins. Mögliche Werte sind:

    Wert     | Beschreibung
    -------- | ------------
    `public` | Feiertag
    `school` | Schulferien
    `custom` | Benutzerdefinierte Freizeit

**`temporalExpressions`**

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### info-Objekt

Das `info`-Objekt enthält Metadaten zum Stundenplan:

**`title`**

:   Der Titel oder die Bezeichnung des Stundenplans. **Dieses Feld ist ERFORDERLICH**.

**`description`**

:   Eine kurze Beschreibung des Stundenplans

**`summary`**

:   Eine Zusammenfassung des Stundenplaninhalts.

**`publishedAt`**

:   Zeitpunkt der Veröffentlichung des Stundenplans.

**`publishedFrom`**

:   Wem gehört der Stundenplan?

**`language`**

:   Die Ausgabesprache des Stundenplans. Dies MUSS ein [ISO 639-1](https://www.iso.org/iso-639-language-codes.html) Sprachcode sein.

**`source`**

:   Quelle der Stundenplandaten.

**`source.name`**

:   Name des Dienstes, der Anwendung oder des Werkzeugs, mit dessen Hilfe die Stundenplandaten erzeugt wurden. **Dieses Feld ist ERFORDERLICH**.

**`source.version`**

:   Versionsnummer des Dienstes, der Anwendung oder des Werkzeugs, mit dessen Hilfe die Stundenplandaten erzeugt wurden.

**`source.url`**

:   Eine URL, unter der sich weitere Informationen finden lassen.

Dieses Objekt KANN erweitert werden.

Beispiel:

``` json
"info": {
  "title": "Stundenplan 2023/2024",
  "description": "Stundenplan für das Schuljahr 2023/2024",
  "summary": "Der aktuelle Stundenplan inklusive Aufsichten und Vertretungen.",
  "version": "201",
  "publishedAt": "2023-09-01T12:00:00",
  "publishedFrom": "Meine-Schule, Berlin",
  "language": "de",
  "source": {
    "name": "MyTimeTableApp",
    "version": "0.2"
  }
}
```

#### lesson-Objekt

Das `lesson`-Objekt repräsentiert eine Veranstaltung bzw. Unterrichtseinheit, die einem Kurs zugeordnet ist und zeitlich verplant wird:

**`type`** 

:   MUSS den Wert `lesson` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Veranstaltung. **Dieses Feld ist ERFORDERLICH**.

**`course.refId`** 

:   Der zugeordnete Kurs. Dies MUSS ein Verweis auf die `id` eines `course`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`relevance`** 

:   Relevanz des Kurses. **Dieses Feld ist ERFORDERLICH**.

    Folgende Werte sind definiert:

    Wert         | Beschreibung
    ------------ | ------------
    `scheduled`  | Wie geplant
    `additional` | Zusatzunterricht

**`notes`** 

:   Bemerkungen zur Veranstaltung.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Veranstaltung.

**`teachingFormat.idRef`** 

:   Unterrichtsformat. Dies MUSS ein Verweis auf die `id` eines `teachingFormat`-Objekts sein. 

**`groups`** 

:   Eine Liste von teilnehmenden Gruppen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `group`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`attendees`** 

:   Eine Liste von Teilnehmern und deren Rollen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `person`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role.refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `personRole`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`rooms`** 

:   Eine Liste von genutzten Räumen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `room`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### oneTimeExpression-Objekt

Das `oneTimeExpression`-Objekt definiert einen einmaligen zeitlichen Ausdruck:

**`type`** 

:   MUSS den Wert `oneTime` haben. **Dieses Feld ist ERFORDERLICH**.

**`startTimepoint`** 

:   Startzeitpunkt (RFC 3339) des zeitlichen Ausdrucks. **Dieses Feld ist ERFORDERLICH**.

**`endTimepoint`** 

:   Endzeitpunkt (RFC 3339) des zeitlichen Ausdrucks. **Dieses Feld ist ERFORDERLICH**.

**`operation`** 

:   Soll der zeitliche Ausdruck hinzugefügt oder abgezogen werden? 

    + **`include`** : Findet statt (das ist der Standardwert)
    + **`exclude`** : Findet nicht statt

Das folgende Beispiel zeigt ein `oneTimeExpression`-Objekt, das sich über mehrere Tage erstreckt:

``` json
"temporalExpressions": [
  {
    "type": "onetime",
    "startTimepoint": "2023-12-23T12:00:00",
    "endTimepoint": "2024-01-05T12:00:00"
  }
]
```

#### person-Objekt

Das `person`-Objekt repräsentiert Mitglieder einer Gruppe bzw. Teilnehmer eines Kurses, einer Veranstaltung, einer Aufsicht eines Ereignisses oder einer Aktivität:

**`id`** 

:   Eindeutige Identifikation der Person. **Dieses Feld ist ERFORDERLICH**.

**`name.shortName`** 

:   Kürzel der Person. **Dieses Feld ist ERFORDERLICH**.

**`name.fullName`** 

:   Der komplett ausgeschriebene Name der Person.

**`name.sortingName`** 

:   Der Name der Person, optimiert für eine gewünschte alphanumerische Sortierung in einer Liste.

**`name.familyName`** 

:   Nachname der Person.

**`name.familyNamePrefix`** 

:   Namensvorsatz (z.B. "von") der Person.

**`name.middleName`** 

:   Mittelnamen der Person. Dies MUSS ein JSON-String-Array sein. 

**`name.givenName`** 

:   Vorname der Person.

**`name.nameSuffix`** 

:   Namenszusätze (z.B. "Jr.") der Person. Dies MUSS ein JSON-String-Array sein. 

**`name.title`** 

:   Titel (z.B. "Dr.") der Person. Dies MUSS ein JSON-String-Array sein. 

**`name.nickName`** 

:   Rufname der Person. 

**`gender.refId`** 

:   Geschlecht der Person. Dies MUSS ein Verweis auf die `id` eines `gender`-Objekts sein. 

**`birthdate`** 

:   Geburtsdatum der Person.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Person.

**`timeFrame`** 

:   Der zugeordnete Zeitrahmen der Person. Dies MUSS ein `reference`-Objekt, das auf ein `timeFrame`-Objekt verweist, sein. Diese Angabe macht nur Sinn, wenn sie vom Standardzeitrahmen des Stundenplans abweicht.

**`externalIds`** 

:   Eine optionale List von externen Identifikatoren. Es MUSS ein JSON-Array mit `externalId`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### personRole-Objekt

Das `personRole`-Objekt repräsentiert einen Rolle, mit der Mitglieder oder Teilnehmer kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation der Rolle. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. **Dieses Feld ist ERFORDERLICH**. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Standardmäßig wird folgende Code-Liste EMPFOHLEN:
    
    CanonicalURI                               | URL
    ------------------------------------------ | ---
    `urn:opene8:school:codelist:de:personRole` | [Link](https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Aschool%3Acodelist%3Ade%3ApersonRole)

**`shortName`** 

:   Kürzel der Rolle. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name der Rolle. 

**`description`** 

:   Eine kurze Beschreibung der Rolle.

Dieses Objekt KANN erweitert werden.

#### room-Objekt

Das `room`-Objekt repräsentiert einen Raum, in dem Unterricht oder ein anderweitiges Ereignis stattfindet:

**`id`** 

:   Eindeutige Identifikation des Raums. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel des Raums. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Raums. 

**`description`** 

:   Eine kurze Beschreibung des Raums.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Raum.

**`building.refId`** 

:   Das Gebäude, in dem sich der Raum befindet. Dies MUSS ein Verweis auf die `id` eines `building`-Objekts sein. 

**`externalIds`** 

:   Eine optionale List von externen Identifikatoren. Es MUSS ein JSON-Array mit `externalId`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### schedule-Objekt

Das `schedule`-Objekt enthält die eigentliche zeitliche Verplanung:

**`validFrom`** 

:   Definiert den Startzeitpunkt (RFC 3339) des Gültigkeit des Stundenplans. **Dieses Feld ist ERFORDERLICH**.

**`validTo`** 

:   Definiert den Endzeitpunkt (RFC 3339) des Gültigkeit des Stundenplans. **Dieses Feld ist ERFORDERLICH**.

**`defaultTimeFrame`** 

:   Verweis auf den Standardzeitrahmen. Dies MUSS ein `reference`-Objekt sein.

**`scheduleElements`** 

:   Eine Liste von Planelementen. Es MUSS ein JSON-Array mit `activity`-Objekten, `announcement`-Objekten, `event`-Objekten, `gap`-Objekten, `holiday`-Objekten, `lesson`-Objekten und/oder `supervision`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### subject-Objekt

Das `subject`-Objekt repräsentiert ein Fach, das mit Kursen verknüpft werden kann:

**`id`** 

:   Eindeutige Identifikation des Fachs. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Standardmäßig wird folgende Code-Liste EMPFOHLEN:
    
    CanonicalURI                            | URL
    --------------------------------------- | ---
    `urn:opene8:school:codelist:de:subject` | [Link](https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Aschool%3Acodelist%3Ade%3Asubject)

**`shortName`** 

:   Kürzel des Fachs. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Fachs. 

**`description`** 

:   Eine kurze Beschreibung des Fachs.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für das Fach.

**`externalIds`** 

:   Eine optionale List von externen Identifikatoren. Es MUSS ein JSON-Array mit `externalId`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### substitution-Objekt

Das `substitution`-Objekt definiert eine Vertretung:

**`type`** 

:   MUSS den Wert `substitution` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Vertretung. **Dieses Feld ist ERFORDERLICH**.

**`notes`** 

:   Bemerkungen zur Vertretung.

**`appliesTo`** 

:   Eine Aktivität, eine Unterrichtseinheit oder eine Aufsicht, welche(n) die Vertretung darstellt. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
    
        Mögliche Werte sind:
    
        Wert          | Beschreibung
        ------------- | ------------
        `activity`    | Vertretung durch eine Aktivität
        `lesson`      | Fehlstelle durch eine Unterrichtseinheit
        `supervision` | Fehlstelle durch eine Aufsicht
        
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `activity`-Objekts, eines vorhandenen `lesson`-Objekts oder eines vorhandenen `supervision`-Objekts sein, jeweils in Abhängigkeit vom Wert in Feld `type`. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### supervision-Objekt

Das `supervision`-Objekt repräsentiert eine Aufsicht, die einem oder mehren Aufsichtsbereichen zugeordnet ist und zeitlich verplant wird:

**`type`** 

:   MUSS den Wert `supervision` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Aufsicht. **Dieses Feld ist ERFORDERLICH**.

**`notes`** 

:   Bemerkungen zur Aufsicht.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Aufsicht.

**`supervisionType.idRef`** 

:   Typ der Aufsicht. Dies MUSS ein Verweis auf die `id` eines `supervisionType`-Objekts sein. 

**`attendees`** 

:   Eine Liste von Teilnehmern und deren Rollen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `person`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role.refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `personRole`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`areas`** 

:   Eine Liste von betroffenen Aufsichtsbereichen. Dies MUSS ein JSON-Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf die `id` eines vorhandenen `supervisionArea`-Objekts sein. **Dieses Feld ist ERFORDERLICH**.

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### supervisionArea-Objekt

Das `supervisionArea`-Objekt repräsentiert ein Aufsichtsbereich, für den Aufsichten verplant werden können:

**`id`** 

:   Eindeutige Identifikation des Aufsichtsbereichs. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel des Aufsichtsbereichs. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Aufsichtsbereichs. 

**`description`** 

:   Eine kurze Beschreibung des Aufsichtsbereichs.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Aufsichtsbereich.

**`campus.refId`** 

:   Der Campus, auf dem sich der Aufsichtsbereich befindet. Dies MUSS ein Verweis auf die `id` eines `campus`-Objekts sein. 

**`externalIds`** 

:   Eine optionale List von externen Identifikatoren. Es MUSS ein JSON-Array mit `externalId`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### supervisionType-Objekt

Das `supervisionType`-Objekt repräsentiert einen Aufsichtstyp, mit dem Aufsichten kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Aufsichtstyp. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Standardmäßig wird keine folgende Code-Liste empfohlen.

**`shortName`** 

:   Kürzel des Aufsichtstyp. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Aufsichtstyp. 

**`description`** 

:   Eine kurze Beschreibung des Aufsichtstyp.

Dieses Objekt KANN erweitert werden.

#### teachingFormat-Objekt

Das `teachingFormat`-Objekt repräsentiert ein Unterrichtsformat, mit dem Unterrichtseinheiten kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Unterrichtsformat. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Ein standardisierter Schlüssel. Dies MUSS ein `externalCode`-Objekt sein, das auf einen Code aus einer externen Code-Liste verweist. 

    Standardmäßig wird folgende Code-Liste EMPFOHLEN:
    
    CanonicalURI                                   | URL
    ---------------------------------------------- | ---
    `urn:opene8:school:codelist:de:teachingFormat` | [Link](https://api.codelisthub.org/v1/documents/urn%3Aopene8%3Aschool%3Acodelist%3Ade%3AteachingFormat)

**`shortName`** 

:   Kürzel des Unterrichtsformat. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Unterrichtsformat. 

**`description`** 

:   Eine kurze Beschreibung des Unterrichtsformat.

Dieses Objekt KANN erweitert werden.

#### timeFrame-Objekt

Das `timeFrame`-Objekt definiert einen Zeitrahmen, mit dessen Hilfe sich die Uhrzeiten der Planelemente auf ein abstrahiertes Raster (z.B. !. Stunde, 2. Stunde, Pause, etc.) abbilden:

**`id`** 

:   Eindeutige Identifikation des Zeitrahmens. **Dieses Feld ist ERFORDERLICH**.

**`shortName`** 

:   Kürzel des Zeitrahmens. **Dieses Feld ist ERFORDERLICH**.

**`longName`** 

:   Ausführlicher Name des Zeitrahmens. 

**`description`** 

:   Eine kurze Beschreibung des Zeitrahmens.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Zeitrahmen.

**`scopeOfWeek`** 

:   Die Menge der Wochentage, die bei einer wöchenlichen Darstellung des Stundenplans berücksichtigt werden sollen (z.B. nur Montag bis Samstag). **Dieses Feld ist ERFORDERLICH**.

    Folgende Werte sind definiert:

    Wert      | Beschreibung
    --------- | ------------
    `mon`     | Montag
    `tue`     | Dienstag
    `wef`     | Mittwoch
    `thu`     | Donnerstag
    `fri`     | Freitag
    `sat`     | Samstag
    `sun`     | Sonntag

**`startOfWeek`** 

:   Der Wochentag, mit dem bei einer wöchenlichen Darstellung des Stundenplans begonnen werden soll. Der Standardwert ist `mon`.

    Folgende Werte sind definiert:

    Wert      | Beschreibung
    --------- | ------------
    `mon`     | Montag
    `tue`     | Dienstag
    `wef`     | Mittwoch
    `thu`     | Donnerstag
    `fri`     | Freitag
    `sat`     | Samstag
    `sun`     | Sonntag

**`timeSlots`** 

:   Eine Liste von benannten Zeitfenstern, welche die Abstraktion des Zeitrahmens definieren. Dies MUSS ein JSON-Array mit `timeSlot`-Objekten sein. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### timeSlot-Objekt

Das `timeSlot`-Objekt definiert ein benanntes Zeitfenster für einen Zeitrahmen (z.B. 1. Stunde von 8:00 bis 8:45):

**`shortlabel`** 

:   Kürzel des Zeitfenster. **Dieses Feld ist ERFORDERLICH**.

**`longlabel`** 

:   Ausführlicher Name des Zeitfenster. 

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für das Zeitfenster.

**`startTime`** 

:   Die Startuhrzeit (RFC 3339) des Zeitfenster. **Dieses Feld ist ERFORDERLICH**.

**`endTime`** 

:   Die Enduhrzeit (RFC 3339) des Zeitfenster. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.


#### weeklyExpression-Objekt

Das `weeklyExpression`-Objekt definiert einen sich wöchentlich wiederholenden zeitlichen Ausdruck:

**`type`** 

:   MUSS den Wert `weekly` haben. **Dieses Feld ist ERFORDERLICH**.

**`startTimepoint`** 

:   Startzeitpunkt (RFC 3339) des zeitlichen Ausdrucks. **Dieses Feld ist ERFORDERLICH**.

**`endTimepoint`** 

:   Endzeitpunkt (RFC 3339) des zeitlichen Ausdrucks. **Dieses Feld ist ERFORDERLICH**.

**`weeks`** 

:   Eine Liste von Kalenderwochen, an denen dieser zeitliche Ausdruck sich wiederholt. Ist dieses Feld nicht definiert, dann wiederholt sich dieser zeitliche Ausdruck in jeder Woche innerhalb der Gültigkeit.

**`validFrom`** 

:   Definiert den Startzeitpunkt (RFC 3339) des Gültigkeit der wöchentlich Wiederholung. Ist dieses Feld nicht definiert, dann gilt der Startzeitpunkt der Gültigkeit des `schedule`-Objekts.

**`validTo`** 

:   Definiert den Endzeitpunkt (RFC 3339) des Gültigkeit der wöchentlich Wiederholung. Ist dieses Feld nicht definiert, dann gilt der Endzeitpunkt der Gültigkeit des `schedule`-Objekts.

**`operation`** 

:   Soll der zeitliche Ausdruck hinzugefügt oder abgezogen werden? 

    + **`inlcude`** : Findet statt (das ist der Standardwert)
    + **`exclude`** : Findet nicht statt

Das folgende Beispiel zeigt ein `weeklyExpression`-Objekt, bei dem für das Jahr 2023 die Kalenderwochen 36,38,40,42,44,46,48 und 50, sowie für das Jahr 2024 die ersten 4 Wochen markiert sind:

``` json
"temporalExpressions": [
  {
    "type": "weekly",
    "startTimepoint": "2023-09-08T10:30:00",
    "endTimepoint": "2023-09-08T11:15:00",
    "weeks": [
      "2023:36,38,40,42,44,46,48,50",
      "2024:1-4"
    ]
  }
]  
```

### Erweiterung der Spezifikation

Die OpenT8-Spezifikation kann an bestimmten Stellen um zusätzliche Daten erweitert werden.

Die Eigenschaften der Erweiterungen sind als freie Felder implementiert, denen immer ein `x-` vorangestellt werden MUSS (z.B. `x-external-id`). Der Wert kann eine Zeichenfolge, eine Zahl, ein boolescher Wert, Null, ein Objekt oder ein Array sein.

Die Erweiterungen können von den verfügbaren Werkzeugen unterstützt werden oder auch nicht. Idealerweise können diese Werkzeuge erweitert werden, um die gewünschte Unterstützung hinzuzufügen (z.B. bei Open Source-Projekten).

Beispiel:

``` json
"buildings": [
  {
    "id": "100",
    "code": "HG",
    "name": "Hauptgebäude",
    "x-postalAddress": "Berliner Weg 42, 30100 Braunschweig",
    "x-website": "https://beispiel.de"
  }
]
```