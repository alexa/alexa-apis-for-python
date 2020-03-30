=========
CHANGELOG
=========

1.0.0
-----

* Initial release of ask smapi models.

1.1.0
~~~~~

This release contains the following changes : 

- Add model definitions for new `APIS related to slot type management <https://developer.amazon.com/en-US/docs/alexa/smapi/create-a-slot-type-to-use-in-multiple-skills.html>`__. Skill developers can create slot types outside the context of a skill and use it across multiple skills.



1.1.1
^^^^^

This release contains the following changes : 

- Updated properties for `skill response <https://developer.amazon.com/en-US/docs/alexa/smapi/skill-operations.html#response-4>`__ in `ListSkills` API.
- Updated interaction model values for `validation rules <https://developer.amazon.com/en-US/docs/alexa/custom-skills/validate-slot-values.html#validation-rules>`__.


1.2.0
~~~~~

This release contains the following changes : 

- APIs and model definitions for new `Audit Logs API <https://developer.amazon.com/en-US/docs/alexa/smapi/audit-logs-api.html>`__. Skill developers can use the Audit Logs API to get logs that show history of calls made to the Skill Management API(SMAPI). The logs include information about each operation including the timestamp, response code, and source.
- APIs and model definitions for new `Skill Simulations V2 API <https://developer.amazon.com/en-US/docs/alexa/smapi/skill-simulation-api.html>`__. The Skill Simulation API enables skill developers to simulate skill execution. You can test your skill and see the intent that a simulated device returns from your interaction model.
