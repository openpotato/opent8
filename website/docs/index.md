# Einführung

OpenT8 ist ein standardisiertes [JSON](https://www.json.org/)-Format zum Abbilden von komplexen Stundenplandaten. 

Die wesentlichen Eigenschaften sind:

+ Open Source
+ OpenT8-Dokumente können gegen das [OpenT8 Document Schema](https://github.com/openpotato/opent8/blob/main/schemas/v0.2/schema.json) validiert werden.
+ Unterstützung von Veranstaltungen jeglicher Art (z.B. Unterricht, Prüfungen, Treffen etc.)
+ Unterstützung von Teilnehmern jeglicher Art (z.B. Lehrer:in, Schüler:in, Erzieher:in etc.)
+ Unterstützung von Planänderungen (Vertretungen, Verschiebungen, Ausfall etc.)
+ Unterstützung von Aufsichten
+ Unterstützung von Schulferien und Feiertagen
+ Unterstützung von Zeitrahmen (Von wann bis wann geht die erste Stunde am Tag? Wann ist Mittagspause? etc.)
+ Unterstützung von Farbdefinitionen
+ Flexible Definition der Zeitplanung durch zeitliche Ausdrücke
+ Erweiterungen durch benutzerdefinierte Eigenschaften möglich

Der Namensbestandteil T8 leitet sich aus dem englischen Begriff für Stundenplan - *Timetable* - ab: Die Zahl 8 repräsentiert die Anzahl der Zeichen nach dem T.

## Beispiele

Die folgenden OpenT8-Beispiel-Dokumente stehen zur Verfügung:

+ [Beispiel für Grundschule](https://github.com/openpotato/opent8/blob/main/samples/sample.de.grundschule.json)

## Aktueller Status

OpenT8 ist noch relativ frisch und hier bereits in einer zweiten Version veröffentlicht. Über [Feedback](community.md) jeglicher Art würden wir uns sehr freuen.