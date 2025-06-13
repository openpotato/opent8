# Änderungslog

## 0.5.0 <small>_ 12. Juni 2025</small>

**Hinzugefügt**:

+ Neue Entität `weeksPattern` hinzugefügt.

**Geändert:**

+ Breaking change: Die Eigenschaft `weeklyExpression.weeks` wurde umbenannt in `weeklyExpression.validWeeks`.
+ Die Eigenschaft `weeklyExpression.validWeeks` ist jetzt polymorph. Sie ist entweder (wie bisher) ein JSON-String-Array oder (jetzt neu) ein JSON-Objekt mit einem Verweis auf eine `weeksPattern`-Entität.

## 0.4.0 <small>_ 10. April 2025</small>

**Geändert:**

+ Breaking change: Die Eigenschaft `person.name` wurde refactored, um sie kompatibel zu machen mit der XÖV-Kernkomponente [NameNatuerlichePerson](https://www.xrepository.de/details/urn:xoev-de:kosit:xoev:kernkomponente:namenatuerlicheperson).

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

+ Breaking change: Die Eigenschaft `holiday.holidayType` ist jetzt erforderlich.
+ Breaking change: Die Eigenschaft `person.name.middleName` wurde umbenannt in `person.name.middleNames`.
+ Breaking change: Die Eigenschaft `person.name.nameSuffix` wurde umbenannt in `person.name.nameSuffixes`.
+ Breaking change: Die Eigenschaft `person.name.title` wurde umbenannt in `person.name.titles`.
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

+ Breaking change: `stash` wurde in `exemption` umbenannt. 
+ Breaking change: In fast allen Fällen wurden die bisherigen Eignschaften `code` und `name` entweder in `shortName` und `longName` oder in `shortDescription` und `longDescription` umbenannt.
+ Breaking change: In einigen Fällen wurde die bisherigen Eignschaft `description` in `notes` umbenannt.
+ Breaking change: In allen Fällen wurde die String-Unterscheidung in `singular` und `plural` aufgelöst.
+ Breaking change: Refactoring der Eigenschaften bei `absence`. Die Eigenschaft `absenceType` ist neu.
+ Breaking change: Refactoring der Eigenschaften bei `course`. Die Eigenschaften `courseUrl` und `courseNo` sind neu. Die Eigenschaft `courseType` ist jetzt eine eigene Entität.
+ Breaking change: Refactoring der Eigenschaften bei `event`. Die Eigenschaft `eventType` ist neu.
+ Breaking change: Refactoring der Eigenschaften bei `exemption`. Die Eigenschaft `exemptionType` ist neu.
+ Breaking change: Refactoring der Eigenschaften bei `group`. Die Eigenschaft `groupType` ist jetzt eine eigene Entität.
+ Breaking change: Refactoring der Eigenschaften bei `lesson`. Die Eigenschaften `relevance` und `teachingForm` sind neu.
+ Breaking change: Refactoring der Eigenschaften bei `person`. Neu ist `gender`. Die Namenseigenschaften wurden zudem komplett überarbeitet.
+ Breaking change: Refactoring der Eigenschaften bei `supervision`. Die Eigenschaft `supervisionType` ist neu.
+ Breaking change: Zahlreiche weitere kleinere Refactorings und Umbenennungen

**Anmerkung**:

Diese Version sollte jetzt einigermaßen stabil bleiben.

## 0.1.0 <small>_ 20. November 2023</small>

**Geändert**:

+ Breaking change: Operationen von zeitlichen Ausdrücken umbenannt zu `include` und `exclude`.

## 0.0.1 <small>_ 18. September 2023</small>

+ Erste Veröffentlichung