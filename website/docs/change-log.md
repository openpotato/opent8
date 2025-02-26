# Änderungslog

## OpenT8-Spezifikation

### 0.2.0 <small>_ 24. Febnruar 2025</small>

+ Neue Entitäten `absenceType`, `activity`, `activityType`, `courseType`, `eventType`, `exemptionType`, `gender`, `groupType`, `supervisionType` und `teachingFormat`
+ Die Eigenschaft `code` als Verweis auf Code-Listen im OpenCodeList-Format ist neu für `absenceType`, `activityType`, `courseType`, `eventType`, `exemptionType`, `gender`, `groupType`, `personRole`, `subject`, `supervisionType` und `teachingFormat`.
+ Die Eigenschaft `externalIds` ist neu für `campus`, `building`, `room`, `course`, `person`, `group`, `supervisionArea`.
+ [Breaking change]: `stash` wurde in `exemption` umbenannt. 
+ [Breaking change]: In fast allen Fällen wurden die bisherigen Eignschaften `code` und `name` entweder in `shortName` und `longName` oder in `shortDescription` und `longDescription` umbenannt.
+ [Breaking change]: In einigen Fällen wurde die bisherigen Eignschaft `description` in `notes` umbenannt.
+ [Breaking change]: In allen Fällen wurde die String-Unterscheidung in `singular` und `plural` aufgelöst.
+ [Breaking change]: Refactoring der Eigenschaften bei `absence`. Die Eigenschaft `absenceType` ist neu.
+ [Breaking change]: Refactoring der Eigenschaften bei `course`. Die Eigenschaften `courseUrl` und `courseNo` sind neu. Die Eigenschaft `courseType` ist jetzt eine eigene Entität.
+ [Breaking change]: Refactoring der Eigenschaften bei `event`. Die Eigenschaft `eventType` ist neu.
+ [Breaking change]: Refactoring der Eigenschaften bei `exemption`. Die Eigenschaft `exemptionType` ist neu.
+ [Breaking change]: Refactoring der Eigenschaften bei `group`. Die Eigenschaft `groupType` ist jetzt eine eigene Entität.
+ [Breaking change]: Refactoring der Eigenschaften bei `lesson`. Die Eigenschaften `relevance` und `teachingForm` sind neu.
+ [Breaking change]: Refactoring der Eigenschaften bei `person`. Neu ist `gender`. Die Namenseigenschaften wurden zudem komplett überarbeitet.
+ [Breaking change]: Refactoring der Eigenschaften bei `supervision`. Die Eigenschaft `supervisionType` ist neu.
+ Zahlreiche weitere kleinere Refactorings, Umbenennungen und Bug fixes

Diese Version sollte jetzt einigermaßen stabil bleiben.

### 0.1.0 <small>_ 20. November 2023</small>

+ Operationen von zeitlichen Ausdrücken umbenannt zu `include` und `exclude`.

### 0.0.1 <small>_ 18. September 2023</small>

+ Erste Veröffentlichung