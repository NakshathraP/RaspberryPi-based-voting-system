# RaspberryPi-based-voting-system

A voting system which uses RaspberryPi and RFID cards to ensure security and fairness.

The codes respective of the RFID tags are stored in a MariaDB database of the RaspberryPi system. The system includes three candidate options (buttons) to choose from. The respective vote is added to a counter associated with the candidate. A buzzer is added to indicate if the vote has been registered. An EM-18 reader module is used to read the RFID tags.

The system also verifies if the RFID tag is valid by querying the database. If the tag does not exist in the database, the buzzer sounds countinously until it is manually stopped.

![IMG_20221017_152213](https://github.com/NakshathraP/RaspberryPi-based-voting-system/assets/119211023/16bd3629-9fa0-4917-87bf-53e715a303f0)


https://github.com/NakshathraP/RaspberryPi-based-voting-system/assets/119211023/61c7b336-58c3-48d2-95d2-944e7b1ff151

