# Änderungslog

## 0.2.0 <small>_ 26. Febnruar 2025</small>

**Hinzugefügt**:

+ Neue Entitäten `absenceType`, `activity`, `activityType`, `courseType`, `eventType`, `exemptionType`, `gender`, `groupType`, `supervisionType` und `teachingFormat`
+ Die Eigenschaft `code` als Verweis auf Code-Listen im OpenCodeList-Format ist neu für `absenceType`, `activityType`, `courseType`, `eventType`, `exemptionType`, `gender`, `groupType`, `personRole`, `subject`, `supervisionType` und `teachingFormat`.
+ Die Eigenschaft `externalIds` ist neu für `campus`, `building`, `room`, `course`, `person`, `group`, `supervisionArea`.

**Geändert (breaking changes)**:

+ `stash` wurde in `exemption` umbenannt. 
+ In fast allen Fällen wurden die bisherigen Eignschaften `code` und `name` entweder in `shortName` und `longName` oder in `shortDescription` und `longDescription` umbenannt.
+ In einigen Fällen wurde die bisherigen Eignschaft `description` in `notes` umbenannt.
+ In allen Fällen wurde die String-Unterscheidung in `singular` und `plural` aufgelöst.
+ Refactoring der Eigenschaften bei `absence`. Die Eigenschaft `absenceType` ist neu.
+ Refactoring der Eigenschaften bei `course`. Die Eigenschaften `courseUrl` und `courseNo` sind neu. Die Eigenschaft `courseType` ist jetzt eine eigene Entität.
+ Refactoring der Eigenschaften bei `event`. Die Eigenschaft `eventType` ist neu.
+ Refactoring der Eigenschaften bei `exemption`. Die Eigenschaft `exemptionType` ist neu.
+ Refactoring der Eigenschaften bei `group`. Die Eigenschaft `groupType` ist jetzt eine eigene Entität.
+ Refactoring der Eigenschaften bei `lesson`. Die Eigenschaften `relevance` und `teachingForm` sind neu.
+ Refactoring der Eigenschaften bei `person`. Neu ist `gender`. Die Namenseigenschaften wurden zudem komplett überarbeitet.
+ Refactoring der Eigenschaften bei `supervision`. Die Eigenschaft `supervisionType` ist neu.
+ Zahlreiche weitere kleinere Refactorings und Umbenennungen

**Anmerkung**:

Diese Version sollte jetzt einigermaßen stabil bleiben.

## 0.1.0 <small>_ 20. November 2023</small>

**Geändert (breaking changes)**:

+ Operationen von zeitlichen Ausdrücken umbenannt zu `include` und `exclude`.

## 0.0.1 <small>_ 18. September 2023</small>

+ Erste Veröffentlichung