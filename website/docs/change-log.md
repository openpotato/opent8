# Änderungslog

## 0.7.0 <small>_ 20. August 2026</small>

**Hinzugefügt**:

+ Die Eigenschaften `activity.classification` und `supervision.classification` sind jeweils um den Wert `additional` erweitert worden.

**Geändert**:

+ Breaking Change: Die Eigenschaft `temporalExpressions` ist jetzt überall durchgehend erforderlich.

    + *Begründung*: Ein Zeitelement ohne Zeitangaben macht keinen Sinn.

**Korrigiert**:

+ Es wurden einige Fehler in der Dokumentation und in der Beispieldatei korrigiert.

## 0.6.0 <small>_ 13. Mai 2026</small>

**Hinzugefügt**:

+ Die Entität `person` hat eine zusätzliche optionale Eigenschaft `electronicAddresses` (z.B. für E-Mail-Adressen und Telefonnummern) erhalten.
+ Die Entität `activity` hat eine zusätzliche optionale Eigenschaft `activityUrl` erhalten.
+ Die Entität `event` hat eine zusätzliche optionale Eigenschaft `eventUrl` erhalten.
+ Die Entitäten `group` und `course` haben die zusätzlichen optionalen Eigenschaften `validFrom` und `validTo` erhalten.
+ Die fehlenden Eigenschaften `activity.classification` und `supervision.classification` wurden im Schema hinzugefügt. Beide waren zuvor bereits unter `activity.relevance` und `supervision.relevance` dokumentiert. Siehe hierzu auch den Absatz zu `lesson.classification` im nächsten Abschnitt.

**Geändert**:

+ Breaking Change: Die Eigenschaft `behaviour` wurde umbenannt in `behavior`. Die Eigenschaft `realisedBy` wurde umbenannt in `realizedBy`. 

    + *Begründung*: Die Bezeichner `behaviour` und `realisedBy` entsprechen dem britischen Englisch. In unseren übrigen Benennungen verwenden wir jedoch amerikanisches Englisch. Durchaus diskutabel 😊 Aber wenn, dann sollte man sich durchgehend für *eine* sprachliche Variante entscheiden.

+ Breaking Change: Die Eigenschaften `appliesTo.type` wurden umbenannt in `appliesTo.refType`. Die Eigenschaft `realizedBy.type` wurde umbenannt in `realizedBy.refType`

    + *Begründung*: Der Bezeichner `type` fungiert als Diskriminator für die eigene Entität, während `refType` den Diskriminator der referenzierten Entität beschreibt. Die Umbenennung arbeitet den semantischen Unterschied deutlicher heraus.

+ Breaking Change: Die Eigenschaft `lesson.relevance` wurde umbenannt in `lesson.classification`. 

    + *Begründung*: Der Bezeichner `relevance` suggeriert, dass es sich hierbei um mehr oder weniger relevante Unterrichtseinheiten handelt. Dies ist jedoch nicht der Fall. Der Bezeichner `classification` ist neutraler und daher wesentlich besser geeignet.

+ Breaking Change: Die Eigenschaft `info.publishedFrom` wurde umbenannt in `info.publishedBy`. 

    + *Begründung*: Der Bezeichner `publishedBy` (deutsch: "veröffentlicht von") ist in diesem Kontext semantisch deutlich passender.

**Korrigiert**:

+ Es wurden eine Reihe kleinerer syntaktischer Fehler in der Schemadefinition behoben.

## 0.5.1 <small>_ 06. Januar 2026</small>

**Hinzugefügt**:

+ Die Entitäten `cancellation` und `substitution` haben eine zusätzliche Eigenschaft `message` erhalten.

## 0.5.0 <small>_ 12. Juni 2025</small>

**Hinzugefügt**:

+ Neue Entität `weeksPattern` hinzugefügt.

**Geändert:**

+ Breaking Change: Die Eigenschaft `weeklyExpression.weeks` wurde umbenannt in `weeklyExpression.validWeeks`.
+ Die Eigenschaft `weeklyExpression.validWeeks` ist jetzt polymorph. Sie ist entweder (wie bisher) ein JSON-String-Array oder (jetzt neu) ein JSON-Objekt mit einem Verweis auf eine `weeksPattern`-Entität.

## 0.4.0 <small>_ 10. April 2025</small>

**Geändert:**

+ Breaking Change: Die Eigenschaft `person.name` wurde refactored, um sie kompatibel zu machen mit der XÖV-Kernkomponente [NameNatuerlichePerson](https://www.xrepository.de/details/urn:xoev-de:kosit:xoev:kernkomponente:namenatuerlicheperson).

## 0.3.1 <small>_ 08. April 2025</small>

**Hinzugefügt**:

+ Neue Eigenschaft `activity.groups` hinzugefügt.
+ Neue Eigenschaft `event.groups` hinzugefügt.

## 0.3.0 <small>_ 28. März 2025</small>

**Hinzugefügt**:

+ Die Eigenschaft `lesson.relevance` hat einen zusätzlichen Wert `substitution` bekommen.
+ Neue Eigenschaft `activity.relevance` hinzugefügt.
+ Neue Eigenschaft `supervision.relevance` hinzugefügt.

**Geändert**:

+ Breaking Change: Die Eigenschaft `holiday.holidayType` ist jetzt erforderlich.
+ Breaking Change: Die Eigenschaft `person.name.middleName` wurde umbenannt in `person.name.middleNames`.
+ Breaking Change: Die Eigenschaft `person.name.nameSuffix` wurde umbenannt in `person.name.nameSuffixes`.
+ Breaking Change: Die Eigenschaft `person.name.title` wurde umbenannt in `person.name.titles`.
+ Die Eigenschaft `code` als Verweis auf Code-Listen im OpenCodeList-Format ist jetzt für *alle* Entitäten optional. 

## 0.2.1 <small>_ 08. März 2025</small>

**Geändert**:

+ Ein paar kleinere Refactorings im Schema.

**Korrigiert**:

+ Nicht benötigte Eigenschaft in Entität `timeFrame` entfernt.

## 0.2.0 <small>_ 26. Februar 2025</small>

**Hinzugefügt**:

+ Neue Entitäten `absenceType`, `activity`, `activityType`, `courseType`, `eventType`, `exemptionType`, `gender`, `groupType`, `supervisionType` und `teachingFormat`
+ Die Eigenschaft `code` als Verweis auf Code-Listen im OpenCodeList-Format ist neu für `absenceType`, `activityType`, `courseType`, `eventType`, `exemptionType`, `gender`, `groupType`, `personRole`, `subject`, `supervisionType` und `teachingFormat`.
+ Die Eigenschaft `externalIds` ist neu für `campus`, `building`, `room`, `course`, `person`, `group`, `supervisionArea`.

**Geändert**:

+ Breaking Change: `stash` wurde in `exemption` umbenannt. 
+ Breaking Change: In fast allen Fällen wurden die bisherigen Eigenschaften `code` und `name` entweder in `shortName` und `longName` oder in `shortDescription` und `longDescription` umbenannt.
+ Breaking Change: In einigen Fällen wurde die bisherigen Eigenschaft `description` in `notes` umbenannt.
+ Breaking Change: In allen Fällen wurde die String-Unterscheidung in `singular` und `plural` aufgelöst.
+ Breaking Change: Refactoring der Eigenschaften bei `absence`. Die Eigenschaft `absenceType` ist neu.
+ Breaking Change: Refactoring der Eigenschaften bei `course`. Die Eigenschaften `courseUrl` und `courseNo` sind neu. Die Eigenschaft `courseType` ist jetzt eine eigene Entität.
+ Breaking Change: Refactoring der Eigenschaften bei `event`. Die Eigenschaft `eventType` ist neu.
+ Breaking Change: Refactoring der Eigenschaften bei `exemption`. Die Eigenschaft `exemptionType` ist neu.
+ Breaking Change: Refactoring der Eigenschaften bei `group`. Die Eigenschaft `groupType` ist jetzt eine eigene Entität.
+ Breaking Change: Refactoring der Eigenschaften bei `lesson`. Die Eigenschaften `relevance` und `teachingForm` sind neu.
+ Breaking Change: Refactoring der Eigenschaften bei `person`. Neu ist `gender`. Die Namenseigenschaften wurden zudem komplett überarbeitet.
+ Breaking Change: Refactoring der Eigenschaften bei `supervision`. Die Eigenschaft `supervisionType` ist neu.
+ Breaking Change: Zahlreiche weitere kleinere Refactorings und Umbenennungen

**Anmerkung**:

Diese Version sollte jetzt einigermaßen stabil bleiben.

## 0.1.0 <small>_ 20. November 2023</small>

**Geändert**:

+ Breaking Change: Operationen von zeitlichen Ausdrücken umbenannt zu `include` und `exclude`.

## 0.0.1 <small>_ 18. September 2023</small>

+ Erste Veröffentlichung