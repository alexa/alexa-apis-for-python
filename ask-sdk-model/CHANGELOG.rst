=========
CHANGELOG
=========

0.1
---

* Initial release of models.

0.1.1
~~~~~

* Docstring changes for generated docs.

0.2
---

* APIs for customer contact permissions (CCP).

0.2.1
~~~~~

* Bug fixes, removed incorrect models.

0.3.0
~~~~~

* APIs for getting device timezone, distance measurement, temperature measurement

1.0.0
-----

* Production release of ASK Models Package.

1.1.0
~~~~~

* Models for "Consumables" in In-Skill Products.

* APIs for Amazon Pay V2 that includes :

  - No consent token requirement in request.
  - Have billing address details for eligible Amazon Pay merchants in Response.
  - Permission scope addition to Permissions object.

* Update Skill Event Models to include additional attributes like 'eventPublishingTime' etc.

1.2.0
~~~~~

* Models for "PrintRequest" and "ReservationRequest" in Skill Connections.

1.3.0
~~~~~

* Models for "Alexa Presentation Language". The Alexa Presentation Language
  (APL) enables you to build interactive voice experiences that include
  graphics, images, slideshows, and video, and to customize them for
  different device types.



1.4.0
~~~~~~~

This release includes the following:
- Models for [CanFulfillIntentRequest, for Name-free Interactions](https://developer.amazon.com/docs/custom-skills/implement-canfulfillintentrequest-for-name-free-interaction.html)


1.5.0
~~~~~~~

This release includes the following : 

- Models for Location Services.
- Updated models for Game engine interface.


1.5.1
^^^^^^^

This release includes the following:

- Updated interfaces for Location Services


1.6.0
~~~~~~~

This release includes the following : 

- Models for Reminders


1.6.1
^^^^^^^

This release contains the following changes:

- Updated enum values for Reminder Status
- Updated OutputSpeech model


1.6.2
^^^^^^^

This release contains the following : 

- Updated enum values for APL components.


1.7.0
~~~~~~~

This release contains the following changes : 

- Support for proactive event calls from out of skill session.
- Remove delete reminders support.


1.8.0
~~~~~~~

This release contains the following changes :

- Introduces support for customizing your skill's experience for Echo Auto, which is now shipping to select customers via our invite program, and vehicles and other aftermarket devices that support Alexa Auto.
- The automotive experience introduces another way for customers to interact with skills, while they are on-the-go and their attention is on the road. Now you can adapt your skill experience to be succinct, location-aware, and adaptive to your customer's needs while they're outside the home.


1.9.0
~~~~~~~

This release contains the following changes : 

- Dynamic entities for customized interactions
- Add additional 'entitlementReason' field in In-Skill products


1.10.0
~~~~~~~

This release contains the following changes :

- The `Skill Messaging API <https://developer.amazon.com/docs/smapi/skill-messaging-api-reference.html>`__ is now supported. Use the Skill Messaging API to send a message request to a skill for a specified user. 
- Adds support for additional `APL Standard Commands <https://developer.amazon.com/docs/alexa-presentation-language/apl-standard-commands.html>`__.
- Packaged type information in models as per `PEP 0561 <https://www.python.org/dev/peps/pep-0561/>`__.


1.10.1
^^^^^^^

This release includes the following : 

- Fixing the imports under `reminder_management` service, to deserialize the reminders correctly.



1.10.2
^^^^^^^

- Added video codecs information in the APL Viewport Characteristic `Video property <https://developer.amazon.com/docs/alexa-presentation-language/apl-viewport-characteristics.html#video>`__. 
