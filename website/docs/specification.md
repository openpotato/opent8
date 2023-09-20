# OpenT8-Spezifikation

#### Version 0.0.1

Die Schlüsselwörter "MUSS/MÜSSEN" (*Englisch: "MUST"*), "ERFORDERLICH" (*Englisch: "REQUIRED"*), "EMPFOHLEN" (*Englisch: "RECOMMENDED"*), "SOLLTE" (*Englisch: "SHOULD"*), "SOLLTE NICHT" (*Englisch: "SHOULD NOT"*) und "KANN" *(Englisch: "MAY"*) in diesem Dokument sind so zu interpretieren, wie sie in ihrer englischen Übersetzung in [RFC2119 und RFC8174](https://tools.ietf.org/html/bcp14) spezifiziert sind, und nur dann, wenn sie, wie hier, in Großbuchstaben geschrieben sind.

Dieses Spezifikation ist lizenziert unter der [Apache License, Version 2.0](https://opensource.org/license/apache-2-0/).

## Einführung

OpenT8 definiert ein Standard-Datenformat zur Repräsentation von Stundenplandaten, unabhängig von ihrer Herkunft. Basierend auf dem [JSON-Standard](https://datatracker.ietf.org/doc/html/rfc8259) kann dieses Format mit nahezu jeder Programmiersprache leicht erzeugt und gelesen werden. Mit Hilfe des [OpenT8 Document Schema](https://github.com/openpotato/opent8/tree/main/schemas/v0.1/schema.json) können Dokumente im OpenT8-Format auf ihre syntaktische Korrektheit hin validiert werden.

OpenT8 kann zum Austausch von Stundenplandaten zwischen Diensten oder Anwendungen genutzt werden, als Quelle für die grafische Anzeige von Stundenplänen oder als Antwortformat für API-Anfragen (z.B. für RESTful Web-Services).

## Definitionen

### OpenT8-Dokument

Ein OpenT8-Dokument ist eine in sich geschlossene Ressource, die einen Stundenplan oder Dienstplan definiert und beschreibt. Es MÜSSEN mindestens die Felder `opent8`, `source` und `schedule` enthalten sein. Ein OpenT8-Dokument verwendet die OpenT8-Spezifikation und ist mit ihr konform.

### Teilnehmer

Teilnehmer (*Englisch: attendee*) sind Personen (*Englisch: person*), die Gruppen, Kursen, Veranstaltungen, Aufsichten oder Ereignissen zugeordnet werden. Die Art der Teilnahme wird dabei jeweils durch ihre Rolle (*Englisch: role*) unterschieden (z.B. Lehrer:in, Erzieher:in, Schüler:in, etc.).

Hier ein Beispiel für die Kursteilnahme eines Lehrers:

``` json
"persons": [
  {
    "id": "Leo",
    "code": "Leo",
    "lastName": "Schnitzewitz",
    "middleName": "Alexander",
    "firstName": "Leopold",
    "namePrefix": "Dr.",
    "nameQualifier": "von",
    "birthdate": "1969-07-20"
  }
],
"roles": [
  {
    "id": "LK",
    "code": "LK",
    "key": "DE.LEHR",
    "name": {
      "singular": "Lehrer:in",
      "plural": "Lehrer:innen"
    }
  }
],
"courses": [
  {
    "id": "DE-1A",
    "code": "DE",
    "name": "Deutsch",
    "subject": {
      "refId": "DE"
    },
    "attendees": [
      {
        "refId": "Leo",
        "role": {
          "refId": "LK"
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
    "id": "1a",
    "code": "1a",
    "name": "Klasse 1a",
    "groupType": {
      "refId": "KL"
    }
  },
  {
    "id": "1b",
    "code": "1b",
    "name": "Klasse 1b",
    "groupType": {
      "refId": "KL"
    }
  }
],
"groupTypes": [
  {
    "id": "KL",
    "code": "KL",
    "key": "DE.KLAS",
    "name": {
      "singular": "Klasse",
      "plural": "Klassen"
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
    "code": "DE",
    "name": "Deutsch",
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
    "code": "MU",
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
    "code": "Aufsicht",
    "name": "Pausenaufsicht",
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

#### Ereignisse

Ereignisse (*Englisch: event*) sind Termine, die nicht durch Veranstaltungen oder Aufsichten repräsentiert werden können (z.B. Meetings, Prüfungen, etc.).

Hier ein Beispiel für ein Meeting:

``` json
"scheduleElements": [
  {
    "type": "event",
    "id": "meet-1",
    "code": "Meeting",
    "name": "Abstimmung zur Einschulung",
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
    "id": "KL",
    "code": "KL",
    "name": {
      "singular": "Konferenz",
      "plural": "Konferenzen"
    }
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
    "code": "WeiFe",
    "name": "Weihnachtsferien",
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
    "code": "alarm",
    "name": "Feueralarmübung",
    "description": "Feueralarmübung am Morgen",
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

Fehlstellen (*Englisch: gap*) repräsentieren Veranstaltungen oder Aufsichten, die nicht wie geplant stattfinden können. Eine Fehlstelle definiert neben der Zeit die Gründe (*Englisch: reason*) für die Planänderung (z.B. Lehrer fehlt/ist freigestellt oder Raum ist nicht verfügbar) und die Auflösung (*Englisch: resolution*). Die Auflösung kann entweder eine Vertretung (*Englisch: substitution*) oder der Ausfall (*Englisch: cancellation*) sein.

Hier ein Beispiel für einen Lehrerausfall. Der Unterricht wird durch einen Erzieher vertreten:

``` json
"scheduleElements": [
  {
    "type": "gap",
    "id": "G-1",
    "code": "G-1",
    "description": "Das ist eine Fehlstelle",
	"reference": {
	  "type": "lesson",
	  "refId": "DE-1A"
	},
    "reasons": [
      {
        "type": "absence",
        "id": "A-1",
        "code": "Krank",
        "description": "Lehrer ist krank",
		"reference": {
          "type": "attendee",
          "refId": "Max"
		}
      }
    ],
    "resolutions": [
      {
        "type": "substitution",
        "id": "V-1",
        "code": "Ersatz",
        "description": "Der Erzieher springt ein",
		"reference": {
          "type": "lesson",
          "refId": "Vertretung-1"
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
    "id": "Vertretung-1",
    "code": "Vertretung",
    "description": "Das ist eine Vertretung",
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

Planelemente können mit Standorten verknüpft werden. Für Veranstaltungen und Ereignisse sind dies Räume (*Englisch: room*), für Aufsichten sind dies Aufsichtsbereiche (*Englisch: supervision area*). Räume können für ein Gebäude (*Englisch: building*) zusammengefasst, Gebäude wiederum für einen Campus (*Englisch: campus*) zusammengefasst werden. Auch Aufsichtsbereiche können für einen Campus zusammengefasst werden.

Hier ein Beispiel für zwei Räume mit Verweis auf das gleiche Gebäude:

``` json
"rooms": [
  {
    "id": "100",
    "code": "100",
    "name": "Raum 100",
    "building": {
      "refId": "HG"
    }
  },
  {
    "id": "101",
    "code": "101",
    "name": "Raum 101",
    "building": {
      "refId": "HG"
    }
  }
]
```

### Zeitliche Ausdrücke

Zeitliche Ausdrücke (*Englisch: temporal expression*) erlauben eine flexible zeitliche Planung von Planelementen. 

Die folgenden zeitlichen Ausdeücke werden unterstützt:

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
    "operation": "add"
  },
  {
    "type": "onetime",
    "startTimepoint": "2023-09-22:00:00",
    "endTimepoint": "2023-09-22T00:00:00",
    "operation": "subtract"
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
    "code": "Unterricht",
    "name": "Unterrichtsraster",
    "scopeOfWeek": [
      "mon",
      "tue",
      "wed",
      "thu",
      "fri"
    ],
    "timeSlots": [
      {
        "code": "1",
        "label": "1. Stunde",
        "startTime": "08:00:00",
        "endTime": "08:45:00"
      },
      {
        "code": "2",
        "label": "2. Stunde",
        "startTime": "09:05:00",
        "endTime": "09:50:00"
      },
      {
        "code": "3",
        "label": "3. Stunde",
        "startTime": "10:10:00",
        "endTime": "10:55:00"
      },
      {
        "code": "4",
        "label": "4. Stunde",
        "startTime": "11:00:00",
        "endTime": "11:45:00"
      },
      {
        "code": "5",
        "label": "5. Stunde",
        "startTime": "12:20:00",
        "endTime": "13:05:00"
      }
    ]
  }
]
```

## Spezifikation

### Versionierung

Die OpenT8-Spezifikation wird nach dem Schema `major.minor.patch` versioniert. Der Major-Minor-Teil der Versionsnummer (z. B. `0.1`) MUSS den Funktionssatz der Spezifikation bezeichnen. Die Patch-Versionen betreffen Fehler in diesem Dokument oder stellen Klarstellungen zu diesem Dokument bereit, nicht zum Funktionsumfang. Werkzeuge, die OpenT8 in der Version `0.1` unterstützen, MÜSSEN mit allen `0.1.*` Versionen von OpenT8 kompatibel sein. Die Patch-Version SOLLTE von den Werkzeugen NICHT berücksichtigt werden, so dass zum Beispiel kein Unterschied zwischen `0.1.0` und `0.1.1` gemacht wird.

Ein OpenT8-Dokument enthält stets ein obligatorisches Feld `opent8`, das die verwendete Version der OpenT8-Spezifikation angibt.

### Format

Ein OpenT8-Dokument, das mit der OpenT8-Spezifikation konform ist, ist selbst ein JSON-Objekt, das im JSON-Format dargestellt werden kann.

Bei allen Feldnamen in der Spezifikation wird zwischen Groß- und Kleinschreibung unterschieden. 

Das Schema sieht zwei Arten von Feldern vor: Fest definierte Felder, die einen deklarierten Namen haben, und freie Felder, deren Namen aber einem bestimmten Muster (*Englisch: pattern*) entsprechen MÜSSEN. Zusatzfelder MÜSSEN innerhalb des enthaltenen JSON-Objekts eindeutige Namen haben.

#### JSON Schema

[JSON Schema](https://json-schema.org/) ist eine Spezifikation zur Definition von JSON-Datenstrukturen. Ein JSON-Schema wird selbst deklarativ durch [JSON](https://www.json.org/) ausgedrückt. Das [OpenT8 Document Schema](https://github.com/openpotato/opent8/tree/main/schemas/v0.1/schema.json) ist ein JSON-Schema für OpenT8-Dokumente.

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

Ein Beispiel, bei dem für das Jahr 2023 die Kalenderwochen 36,38,40,42,44,46,48 und 50, sowie für das Jahr 2024 die ersten 4 Wochen markiert sind:

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
+ `#ff8000` ist organge

### Schema

#### OpenT8-Objekt

Dies ist das Wurzelobjekt eines OpenT8-Dokuments und enthält folgende Felder:

**`opent8`**

:   Definiert die Versionsnummer der OpenT8-Spezifikation. **Dieses Feld ist ERFORDERLICH**.

**`info`**

:   Metadaten zum Stundenplan. **Dieses Objekt ist ERFORDERLICH**.

**`persons`**

:   Eine Liste von Personen. Es MUSS ein JSON-Array mit `person`-Objekten sein. 

**`roles`**

:   Eine Liste von Teilnehmerrollen. Es MUSS ein JSON-Array mit `role`-Objekten sein. 

**`groups`**

:   Eine Liste von Gruppen. Es MUSS ein JSON-Array mit `group`-Objekten sein. 

**`groupTypes`**

:   Eine Liste von Gruppentypen. Es MUSS ein JSON-Array mit `groupType`-Objekten sein. 

**`rooms`**

:   Eine Liste von Räumen. Es MUSS ein JSON-Array mit `room`-Objekten sein.  

**`buildings`**

:   Eine Liste von Gebäuden. Es MUSS ein JSON-Array mit `building`-Objekten sein. 

**`campuses`** 

:   Eine Liste von Campus. Es MUSS ein JSON-Array mit `campus`-Objekten sein. 

**`supervisionAreas`** 

:   Eine Liste von Aufsichtsbereichen. Es MUSS ein JSON-Array mit `supervisionArea`-Objekten sein. 

**`eventTypes`** 

:   Eine Liste von Ereignistypen. Es MUSS ein JSON-Array mit `eventType`-Objekten sein. 

**`timeFrames`** 

:   Eine Liste von Zeitrahmen. Es MUSS ein JSON-Array mit `timeFrame`-Objekten sein. 

**`subjects`** 

:   Eine Liste von Fächern. Es MUSS ein JSON-Array mit `subject`-Objekten sein.  

**`courses`** 

:   Eine Liste von Kursen. Es MUSS ein JSON-Array mit `course`-Objekten sein. 

**`schedule`** 

:   Die eigentliche zeitliche Verplanung. **Dieses Objekt ist ERFORDERLICH**.

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
    "version": "1.0"
  }
}
```

#### source-Objekt

Das `source`-Objekt enthält Informationen zum Dienst, zur Anwendung oder zum Werkzeug, mit dessen Hilfe die Stundenplandaten erzeugt wurden:

**`name`**

:   Name des Dienstes, der Anwendung oder des Werkzeugs, mit dessen Hilfe die Stundenplandaten erzeugt wurden. **Dieses Feld ist ERFORDERLICH**.

**`version`**

:   Versionsnummer des Dienstes, der Anwendung oder des Werkzeugs, mit dessen Hilfe die Stundenplandaten erzeugt wurden.

**`url`**

:   Eine URL, unter der sich weitere Informationen finden lassen.

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

:   Eine Liste von Planelementen. Es MUSS ein JSON-Array mit `lesson`-Objekten, `supervision`-Objekten, `event`-Objekten, `holdiay`-Objekten, `announcement`-Objekten und/oder `gap`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### person-Objekt

Das `person`-Objekt repräsentiert einen Teilnehmer einer Gruppe, eines Kurses, einer Veranstaltungen, einer Aufsichten oder eines Ereignisses:

**`id`** 

:   Eindeutige Identifikation des Teilnehmers. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Teilnehmers. **Dieses Feld ist ERFORDERLICH**.

**`lastName`** 

:   Nachname des Teilnehmers.

**`middleName`** 

:   Mittelname des Teilnehmers.

**`firstName`** 

:   Vorname des Teilnehmers.

**`namePrefix`** 

:  Namenspräfix (z.B. "von") des Teilnehmers.

**`nameQualifier`** 

:   Titel (z.B. "Dr.") des Teilnehmers.

**`nameSuffix`** 

:   Namenszusatz (z.B. "Jr.") des Teilnehmers.

**`birthdate`** 

:   Geburtsdatum des Teilnehmers.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Teilnehmer.

**`timeFrame`** 

:   Der Zeitrahmen des Teilnehmers. Dies MUSS ein `reference`-Objekt, das auf ein `timeFrame`-Objekt verweist, sein. Diese Angabe macht nur Sinn, wenn sie vom Standardzeitrahmen des Stundenplans abweicht.

Dieses Objekt KANN erweitert werden.

#### role-Objekt

Das `role`-Objekt repräsentiert einen Rolle, mit der Teilnehmer kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation der Teilnehmerrolle. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Teilnehmerrolle. **Dieses Feld ist ERFORDERLICH**.

**`key`** 

:   Ein standardisierter, optionaler Schlüssel. Es wird **EMPFOHLEN**, diese Werte, wann immer möglich zu verwenden, um eine Kategorisierung der Rolle unabhängig von der Datenquelle zu gewährleisten.

    Folgende Werte sind definiert:

    Wert      | Beschreibung
    --------- | ------------
    `DE.KIND` | Kind 
    `DE.SCHÜ` | Schüler:in
    `DE.STUD` | Student:in
    `DE.LEHR` | Lehrkraft
    `DE.DOZN` | Dozent:in
    `DE.ERZI` | Erzieher:in
    `DE.EZBE` | Erziehungsberechtigte:r

**`name`** 

:   Name oder Bezeichnung der Teilnehmerrolle. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`singular`** : Der Name oder die Bezeichnung im Singular. **Dieses Feld ist ERFORDERLICH**.
    + **`plural`** : Der Name oder die Bezeichnung im Plural. **Dieses Feld ist ERFORDERLICH**.

**`description`** 

:   Eine kurze Beschreibung der Teilnehmerrolle.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Teilnehmerrolle.

Dieses Objekt KANN erweitert werden.

#### group-Objekt

Das `group`-Objekt repräsentiert eine Gruppe, der man Teilnehmer zuordnen kann:

**`id`** 

:   Eindeutige Identifikation der Gruppe. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Gruppe. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der Gruppe.

**`description`** 

:   Eine kurze Beschreibung der Gruppe.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Gruppe.

**`attendees`** 

:   Eine Liste von Teilnehmern und ihren Rollen. Dies MUSS ein Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `attendee`-Objektes sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role`** : Verweis auf eine Teilnehmerrolle. Dies MUSS ein `reference`-Objekt sein. **Dieses Feld ist ERFORDERLICH**.
    
**`groupType`** 

:   Typ der Gruppe. Dies MUSS ein `reference`-Objekt, das auf ein `groupType`-Objekt verweist, sein.

**`timeFrame`** 

:   Der Zeitrahmen des Teilnehmers. Dies MUSS ein `reference`-Objekt, das auf ein `timeFrame`-Objekt verweist, sein. Diese Angabe macht nur Sinn, wenn sie vom Standardzeitrahmen des Stundenplans abweicht.

Dieses Objekt KANN erweitert werden.

#### groupType-Objekt

Das `groupType`-Objekt repräsentiert einen Gruppentyp, mit dem Gruppen kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Gruppentyps. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Gruppentyps. **Dieses Feld ist ERFORDERLICH**.

**`key`** 

:   Ein standardisierter, optionaler Schlüssel. Es wird **EMPFOHLEN**, diese Werte, wann immer möglich zu verwenden, um eine Kategorisierung der Gruppe unabhängig von der Datenquelle zu gewährleisten.

    Folgende Werte sind definiert:

    Wert      | Beschreibung
    --------- | ------------
    `DE.KITA` | KiTa-Gruppe
    `DE.KIGA` | KiGa-Gruppe
    `DE.HORT` | Hortgruppe
    `DE.KLAS` | Klasse
    `DE.JAHR` | Jahrgang

**`name`** 

:   Name oder Bezeichnung des Gruppentyps. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`singular`** : Der Name oder die Bezeichnung im Singular. **Dieses Feld ist ERFORDERLICH**.
    + **`plural`** : Der Name oder die Bezeichnung im Plural. **Dieses Feld ist ERFORDERLICH**.

**`description`** 

:   Eine kurze Beschreibung des Gruppentyps.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Gruppentyps.

Dieses Objekt KANN erweitert werden.

#### room-Objekt

Das `room`-Objekt repräsentiert einen Raum, in dem Unterricht oder ein anderweitiges Ereignis stattfindet:

**`id`** 

:   Eindeutige Identifikation des Raums. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Raums. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Raums.

**`description`** 

:   Eine kurze Beschreibung des Raums.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Raum.

**`building`** 

:   Das Gebäude, in dem sich der Raum befindet. Dies MUSS ein `reference`-Objekt, das auf ein `building`-Objekt verweist, sein. 

Dieses Objekt KANN erweitert werden.

#### building-Objekt

Das `building`-Objekt repräsentiert ein Gebäude, in dem sich Räume befinden:

**`id`** 

:   Eindeutige Identifikation des Gebäudes. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Gebäudes. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Gebäudes.

    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `attendee`-Objektes sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role`** : Die Teilnehmerrolle. Dies MUSS ein `reference`-Objekt sein, das auf ein vorhandenes `attendeeRole`-Objekt verweist. **Dieses Feld ist ERFORDERLICH**.

**`description`** 

:   Eine kurze Beschreibung des Gebäudes.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für das Gebäude.

**`campus`** 

:   Der Campus, auf dem sich das Gebäude befindet. Dies MUSS ein `reference`-Objekt, das auf ein `campus`-Objekt verweist, sein. 

Dieses Objekt KANN erweitert werden.

#### campus-Objekt

Das `campus`-Objekt repräsentiert einen Campus, auf dem sich Gebäude und/oder Aufsichtsbereiche befinden:

**`id`** 

:   Eindeutige Identifikation des Campus. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Campus. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Campus.

**`description`** 

:   Eine kurze Beschreibung des Campus.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Campus.

Dieses Objekt KANN erweitert werden.

#### supervisionArea-Objekt

Das `supervisionArea`-Objekt repräsentiert ein Aufsichtsbereich, für den Aufsichten verplant werden können:

**`id`** 

:   Eindeutige Identifikation des Aufsichtsbereichs. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Aufsichtsbereichs. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Aufsichtsbereichs.

**`description`** 

:   Eine kurze Beschreibung des Aufsichtsbereichs.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Aufsichtsbereich.

**`campus`** 

:   Der Campus, auf dem sich der Aufsichtsbereich befindet. Dies MUSS ein `reference`-Objekt, das auf ein `campus`-Objekt verweist, sein. 

Dieses Objekt KANN erweitert werden.

#### subject-Objekt

Das `subject`-Objekt repräsentiert ein Fach, das mit Kursen verknüpft werden kann:

**`id`** 

:   Eindeutige Identifikation der Fachs. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Fachs. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Fach.

**`description`** 

:   Eine kurze Beschreibung des Fachs.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für das Fach.

Dieses Objekt KANN erweitert werden.

#### course-Objekt

Das `course`-Objekt repräsentiert einen Kurs, in dem sich Gruppen und/oder Teilnehmer treffen und der Veranstaltungen zugeordnet werden kann:

**`id`** 

:   Eindeutige Identifikation des Kurses. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Kurses. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Kurses.

**`description`** 

:   Eine kurze Beschreibung des Kurses.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Kurs.

**`groups`** 

:   Eine Liste von Gruppen. Dies MUSS ein Array mit `reference`-Objekten sein, die wiederum auf ein vorhandenes `group`-Objekt verweisen.

**`attendees`** 

:   Eine Liste von Teilnehmern und ihren Rollen. Dies MUSS ein Array mit Objekten sein, welche folgende Felder besitzen: 
    
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `attendee`-Objektes sein. **Dieses Feld ist ERFORDERLICH**.
    + **`role`** : Die Teilnehmerrolle. Dies MUSS ein `reference`-Objekt sein, das auf ein vorhandenes `attendeeRole`-Objekt verweist. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### timeFrame-Objekt

Das `timeFrame`-Objekt definiert einen Zeitrahmen, mit dessen Hilfe sich die Uhrzeiten der Planelemente auf ein abstrahiertes Raster (z.B. !. Stunde, 2. Stunde, Pause, etc.) abbilden:

**`id`** 

:   Eindeutige Identifikation des Zeitrahmens. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Zeitrahmens. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Zeitrahmens.

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

:   Eine Liste von benannten Zeitfenstern, welche die Abstraktion des Zeitrahmens definieren. Dies MUSS ein Array mit `timeSlot`-Objekten sein. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### timeSlot-Objekt

Das `timeSlot`-Objekt definiert ein benanntes Zeitfenster für einen Zeitrahmen (z.B. 1. Stunde von 8:00 bis 8:45):

**`code`** 

:   Kürzel des Zeitfensters. **Dieses Feld ist ERFORDERLICH**.

**`label`** 

:   Kennzeichnung des Zeitfenster.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für das Zeitfenster.

**`startTime`** 

:   Die Startuhrzeit (RFC 3339) des Zeitfenster. **Dieses Feld ist ERFORDERLICH**.

**`endTime`** 

:   Die Enduhrzeit (RFC 3339) des Zeitfenster. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### lesson-Objekt

Das `lesson`-Objekt repräsentiert eine Veranstaltung, die einem Kurs zugeordnet ist und zeitlich verplant wird:

**`type`** 

:  MUSS den Wert `lesson` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Veranstaltung. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Veranstaltung. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der Veranstaltung.

**`description`** 

:   Eine kurze Beschreibung der Veranstaltung.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Veranstaltung.

**`course`** 

:   Der zugeordnete Kurs. Dies MUSS ein `reference`-Objekt, das auf ein `course`-Objekt verweist, sein. **Dieses Feld ist ERFORDERLICH**.

**`groups`** 

:   Eine Liste von Gruppenreferenzen. Dies MUSS ein Array mit `reference`-Objekten sein. 

**`attendees`** 

:   Eine Liste von Teilnehmerreferenzen. Dies MUSS ein Array mit `attendeeRef`-Objekten sein. 

**`rooms`** 

:   Eine Liste von Raumreferenzen. Dies MUSS ein Array mit `reference`-Objekten sein. 

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### supervision-Objekt

Das `supervision`-Objekt repräsentiert eine Aufsicht, die einem oder mehren Aufsichtsbereichen zugeordnet ist und zeitlich verplant wird:

**`type`** 

:   MUSS den Wert `supervision` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Veranstaltung. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Veranstaltung. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der Veranstaltung.

**`description`** 

:   Eine kurze Beschreibung der Veranstaltung.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Veranstaltung.

**`attendees`** 

:   Eine Liste von Teilnehmerreferenzen. Dies MUSS ein Array mit `attendee`-Objekten sein. 

**`areas`** 

:   Eine Liste von Aufsichtsbereichsreferenzen. Dies MUSS ein Array mit `reference`-Objekten sein. 

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### event-Objekt

Das `event`-Objekt repräsentiert ein Termin, dass sich nicht durch eine Veranstaltung ausdrücken lässt (z.B. eine Prüfung oder ein Meeting):

**`type`** 

:   MUSS den Wert `event` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation des Termins. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Termins. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Termins.

**`description`** 

:   Eine kurze Beschreibung des Termins.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Termin.

**`eventType`** 

:   Die Typisierung des Termins. Dies MUSS ein `reference`-Objekt, das auf ein `eventType`-Objekt verweist, sein.

**`attendees`** 

:   Eine Liste von Teilnehmerreferenzen. Dies MUSS ein Array mit `attendee`-Objekten sein. 

**`rooms`** 

:   Eine Liste von Raumreferenzen. Dies MUSS ein Array mit `reference`-Objekten sein. 

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### eventType-Objekt

Das `eventType`-Objekt repräsentiert einen Ereignistyp, mit dem Ereignisse kategorisiert werden können:

**`id`** 

:   Eindeutige Identifikation des Ereignistyps. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Ereignistyps. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Ereignistyps. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`singular`** : Der Name oder die Bezeichnung im Singular. **Dieses Feld ist ERFORDERLICH**.
    + **`plural`** : Der Name oder die Bezeichnung im Plural. **Dieses Feld ist ERFORDERLICH**.

**`description`** 

:   Eine kurze Beschreibung des Ereignistyps.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für den Ereignistyps.

Dieses Objekt KANN erweitert werden.

#### holiday-Objekt

Das `holiday`-Objekt repräsentiert schulfreie Zeit (Feiertage oder Schulferien):

**`type`** 

:   MUSS den Wert `holiday` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der schulfreie Zeit. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der schulfreie Zeit. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der schulfreie Zeit.

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

#### announcement-Objekt

Das `announcement`-Objekt repräsentiert eine freie Mitteilung im Stundenplan:

**`type`** 

:   MUSS den Wert `announcement` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Mitteilung. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Mitteilung. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der Mitteilung.

**`description`** 

:   Eine kurze Beschreibung der Mitteilung.

**`color`** 

:   Ein Farbwert (Hex-Kodierung) für die Mitteilung.

**`priority`** 

:   Die Priorität der Mitteilung. 

    Folgende Werte sind definiert:

    Wert        | Beschreibung
    ----------- | ------------
    `important` | Wichtig
    `alarm`     | Alarm

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### gap-Objekt

Das `gap`-Objekt repräsentiert eine Fehlstelle im Stundenplan:

**`type`** 

:   MUSS den Wert `gap` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Fehlstelle. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Fehlstelle. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der Fehlstelle.

**`description`** 

:   Eine kurze Beschreibung der Fehlstelle.

**`reference`** 

:   Verweis auf eine Veranstaltung oder eine Aufsicht. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
	
	    Mögliche Werte sind:
    
	    Wert          | Beschreibung
        ------------- | ------------
        `lesson`      | Veranstaltung, die nicht wie geplant stattfinden kann.
        `supervision` | Aufsicht, die nicht wie geplant stattfinden kann.
		
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `lesson`-Objektes oder eines vorhandenen `supervision`-Objektes sein, jeweils in Abhängigkeit vom Wert in Feld `type`.  **Dieses Feld ist ERFORDERLICH**.

**`reasons`** 

:   Eine Liste von Gründen. Es MUSS ein JSON-Array mit `absence`-Objekten und/oder `stash`-Objekten sein. 

**`resolutions`** 

:   Eine Liste von Auflösungen. Es MUSS ein JSON-Array mit `substitution`-Objekten und/oder `cancellation`-Objekten sein. 

**`temporalExpressions`** 

:   Eine Liste von zeitlichen Ausdrücken. Es MUSS ein JSON-Array mit `oneTimeExpression`-Objekten und/oder `weeklyExpression`-Objekten sein. 

Dieses Objekt KANN erweitert werden.

#### absence-Objekt

Das `absence`-Objekt definiert eine Abwesenheit:

**`type`** 

:   MUSS den Wert `absence` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Abwesenheit. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Abwesenheit. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der Abwesenheit.

**`description`** 

:   Eine kurze Beschreibung der Abwesenheit.

**`reference`** 

:   Referenz zu einer Person, einer Gruppe oder einem Raum. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
	
	    Mögliche Werte sind:
    
	    Wert     | Beschreibung
        -------- | ------------
        `person` | Eine teilnehmende Person (z.B. der Lehrer) ist abwesend.
        `group`  | Eine Gruppe is abwesend.
        `room`   | Der Raum steht nicht zur Verfügung.
		
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `person`-Objektes, eines vorhandenen `group`-Objektes oder eines vorhandenen `room`-Objektes sein, jeweils in Abhängigkeit vom Wert in Feld `type`. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### stash-Objekt

Das `stash`-Objekt definiert eine Freistellung:

**`type`** 

:   MUSS den Wert `stash` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Freistellung. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Freistellung. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der Freistellung.

**`description`** 

:   Eine kurze Beschreibung der Freistellung.

**`reference`** 

:   Referenz zu einer Person. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
	
	    Mögliche Werte sind:
    
	    Wert     | Beschreibung
        -------- | ------------
        `person` | Eine teilnehmende Person (z.B. der Lehrer) ist freigestellt.
		
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `person`-Objektes sein. **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### substitution-Objekt

Das `substitution`-Objekt definiert eine Vertretung:

**`type`** 

:   MUSS den Wert `substitution` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation der Vertretung. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel der Vertretung. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung der Vertretung.

**`description`** 

:   Eine kurze Beschreibung der Vertretung.

**`reference`** 

:   Verweis auf eine Veranstaltung oder eine Aufsicht. Dies MUSS ein JSON-Objekt mit folgenden Feldern sein:

    + **`type`** : Die Typisierung des Feldes `refId`. **Dieses Feld ist ERFORDERLICH**.
	
	    Mögliche Werte sind:
    
	    Wert          | Beschreibung
        ------------- | ------------
        `lesson`      | Neue Veranstaltung als Vertretung.
        `supervision` | Neue Aufsicht als Vertretung.
		
    + **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `lesson`-Objektes oder eines vorhandenen `supervision`-Objektes sein, jeweils in Abhängigkeit vom Wert in Feld `type`.  **Dieses Feld ist ERFORDERLICH**.

Dieses Objekt KANN erweitert werden.

#### cancellation-Objekt

Das `cancellation`-Objekt definiert einen Unterrichtsausfall:

**`type`** 

:   MUSS den Wert `cancellation` haben. **Dieses Feld ist ERFORDERLICH**.

**`id`** 

:   Eindeutige Identifikation des Unterrichtsausfalls. **Dieses Feld ist ERFORDERLICH**.

**`code`** 

:   Kürzel des Unterrichtsausfalls. **Dieses Feld ist ERFORDERLICH**.

**`name`** 

:   Name oder Bezeichnung des Unterrichtsausfalls.

**`description`** 

:   Eine kurze Beschreibung des Unterrichtsausfalls.

**`behaviour`** 

:   Mögliches Verhalten

    + **`leaveRoom`** : Den Unterrichtsraum verlassen
    + **`stayInRoom`** : Im Unterrichtsraum bleiben

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

    + **`add`** : Findet statt (das ist der Standardwert)
    + **`subtract`** : Findet nicht statt

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

:   Definiert den Startzeitpunkt (RFC 3339) des Gültigkeit der wöchentlich Wiederholung. Ist dieses Feld nicht definiert, dann gilt der Startzeitpunkt der Gültigkeit des `schedule`-Objektes.

**`validTo`** 

:   Definiert den Endzeitpunkt (RFC 3339) des Gültigkeit der wöchentlich Wiederholung. Ist dieses Feld nicht definiert, dann gilt der Endzeitpunkt der Gültigkeit des `schedule`-Objektes.

**`operation`** 

:   Soll der zeitliche Ausdruck hinzugefügt oder abgezogen werden? 

    + **`add`** : Findet statt (das ist der Standardwert)
    + **`subtract`** : Findet nicht statt

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

#### reference-Objekt

Das `reference`-Objekt definiert einen generischen Verweis auf ein anderes Objekt. Der Typ des Objekt hängt vom Kontext ab:

+ **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen Objektes sein. **Dieses Feld ist ERFORDERLICH**.

#### attendee-Objekt

Das `attendee`-Objekt definiert einen Verweis auf ein `person`-Objekt verbunden mit einer Rolle:

+ **`refId`** : Dies MUSS ein Verweis auf das Feld `id` eines vorhandenen `person`-Objektes sein. **Dieses Feld ist ERFORDERLICH**.
+ **`role`** : Verweis auf eine Teilnehmerrolle. Dies MUSS ein `reference`-Objekt sein. **Dieses Feld ist ERFORDERLICH**.

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