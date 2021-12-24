# MISP Website

This is the repository of MISP website. The current online version of this portal can be found at [misp-project.org](https://www.misp-project.org/).

## Compiling a local version of the website

The MISP website is based on Hugo, a static site generator. If you plan on contributing major changes to the website, it is important to have a local version, so as to test your changes. 

To compile a local version of the website, run the following commands in a terminal:

1. Install all [Hugo and its prerequisites](https://gohugo.io/getting-started/installing/).

2. Clone the misp-website repository
    ```
    git clone https://github.com/MISP/misp-website.git
    ````
3. Init submodules
   ```
   git submodule init
   git submodule update
   ```
4. Change into your new directory
    ```
    cd misp-website
    ```
5. Build the site and make it available on a local server.
    ```
    hugo server
    ```

6. To preview your site in your web browser, navigate to [http://localhost:1313](http://localhost:1313).


## How to deploy the MISP website

TODO figure this out

