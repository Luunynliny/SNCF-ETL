<div id="top"></div>

<!-- PROJECT SHIELDS -->

[![python](https://badges.aleen42.com/src/python.svg)](https://www.python.org/)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

<!-- PROJECT LOGO -->

<br />

<div align="center">
    <a href="https://github.com/Luunynliny/SNCF-Viz">
        <img src="imgs/logo.png" alt="Logo" height="80">
    </a>
    <h3 align="center">SNCF-Viz</h3>
    <p align="center">
        Visualization of France train network
    </p>
</div>

<!-- ABOUT THE PROJECT -->

## About

This project aims to display information on France train network, supervised by the [Société Nationale des Chemin de Fer](https://www.sncf.com).

<p align="right"><a href="#top"><i>back to top</i></a></p>

<!-- GETTING STARTED -->

## Getting started

### Prerequisites

Prior to installing the project, you need to download and setup Git and Docker, referring to the following documentation:

- https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- https://docs.docker.com/engine/install/

### Installation

1. Clone the repository
2. Create a [Mapbox API token](https://docs.mapbox.com/api/accounts/tokens/)
3. Store the token within the ```viz``` directory
```bash
echo "token" > viz/MAPBOX_TOKEN.txt
```
4. Run Docker compose
```bash
docker compose up
```
5. Go to http://0.0.0.0:8050/

<p align="right"><a href="#top"><i>back to top</i></a></p>

<!-- ROADMAP -->

## Roadmap

- [x] Train stations
- [x] Train network
- [ ] Real-time informations

<p align="right"><a href="#top"><i>back to top</i></a></p>

## License

Distributed under the Creative Commons Zero v1.0 Universal License. See `LICENSE`for more information.

<p align="right"><a href="#top"><i>back to top</i></a></p>

<!-- RESOURCES -->

## Resources

Lignes par type. SNCF Open Data. (2020, May 26). https://ressources.data.sncf.com/explore/dataset/lignes-par-type

Liste des Gares. SNCF Open Data. (2022, March 24). https://ressources.data.sncf.com/explore/dataset/liste-des-gares 

<p align="right"><a href="#top"><i>back to top</i></a></p>