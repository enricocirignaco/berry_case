
<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the berry_case and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** enricocirignaco(github_username), berry_case(repo), e.cirignaco@gmail.com(email)
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="./ressources/images/logo.png" alt="Logo" width="120">
  </a>

  <h2 align="center">berry_case</h2>

  <p align="center">
    The open source Raspberry Pi case without compromises made by the community for the communnity
    <br />
    <br />
    <a href="https://github.com/enricocirignaco/berry_case/issues">Report Bug</a>
    ·
    <a href="https://github.com/enricocirignaco/berry_case/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Starting Situation](#starting-situation)
  * [Aim](#aim)
  * [Product Requirements](#product-requirements)
  * [Current Status](#curent-status)
* [Getting Started](#getting-started)
  * [Toolchain](#Toolchain)
  * [Hardware](#hardware)
  * [Firmware](#firmware)
  * [Sofware(Linux)](#software)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project
Develoop and Build an affordable and open source case for the Raspberry Pi 4 to help the users to become more productive then ever.
<img src="./ressources/images/top.png" alt="top_view">

### Starting Situation

Surfing on the net I discovered some very cool case solutions for the RPi4. I almost ordered one of those products (Argon One). But then I realized that when the RPi4 was powered by a Power Bank(almost always in my case)(5V@2.1A) the CPU had some serious throttling problems. So overclocking with this power supply was out of discussion. I searched for alternative battery powered power supply(5.2V@3A). Without success.
At the same time I discovered some interesting Half-solutions:
* [Argon One](https://www.argon40.com/argon-one-raspberry-pi-4-case.html) (very nice design, power button, cooling system)
* [Acrylic Raspberry Pi set-top box kit](https://wiki.52pi.com/index.php/Acrylic_Raspberry_Pi_set-top_box_kit_SKU:_ZP-0098) (all IOs on the back, full dual HDMI)
* [Raspberry Pi RGB Cooling HAT](https://www.yahboom.net/study/RGB_Cooling_HAT) (OLED dipslay with IP address, CPU temp, etc)
* [Adafruit PowerBoost 1000 Charger](https://www.adafruit.com/product/2465) (UPS solution with Li-Ion cell, power supply)

So I decided to take inspiration from all this product and make my own solution! :)

### Aim
Develop and Build an affordable, open source, smart and good looking case for the Raspberry Pi 4.
Make good documentation and a building guide available to everyone so that anyone can build ther own case at home.
Find someone on github to collaborate with (I'm new on the platform).

### Product Reqirements
* Size: max double the footprint of the RPi4. Max height not defined.
* Battery: min 2 hours of battery life.
* Cooling System: capable of cooling Overclocked RPi4.
* Power Button: capable of Soft and Hard Shutdown.
* PSU: UPS, BMS and 5.2V@min 2A output supply.
* Accessible GPIOs

### Current Status

## Getting Started
### Toolchain

* [Altium Designer 20](https://altium.com)
* [Visual Studio Code](https://code.visualstudio.com/)
* [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html)
* [Autodesk Fuson 360](https://www.autodesk.com/products/fusion-360/overview)

### Hardware

### Firmware

### Software (Linux)
To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
```sh
npm install npm@latest -g
```

### Installation
 
1. Clone the berry_case
```sh
git clone https://github.com/enricocirignaco/berry_case.git
```
2. Install NPM packages
```sh
npm install
```

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_





<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

I'm looking for someone that want to collaborate in this project. I would like to get in touch with you if you are interested. :)

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Enrico Cirignaco - e.cirignaco@gmail.com

Project Link: [https://github.com/enricocirignaco/berry_case](https://github.com/enricocirignaco/berry_case)
