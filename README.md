# MISP Website

This is the repository of MISP website. The current online version of this portal can be found at [misp-project.org](https://www.misp-project.org/).

## Compiling a local version of the website

The MISP website is based on Jekyll, a static site generator. If you plan on contributing major changes to the website, it is important to have a local version, so as to test your changes. 

To compile a local version of the website, run the following commands in a terminal:

1. Install all [Jekyll and its prerequisites](https://jekyllrb.com/docs/installation/), including the bundler [gems](https://jekyllrb.com/docs/ruby-101/#gems). 

2. Clone the misp-website repository
    ```
    git clone https://github.com/MISP/misp-website.git
    ````
3. Change into your new directory
    ```
    cd misp-website
    ```
4. Install missing gems:
    ```
    bundle install
    ```
5. Build the site and make it available on a local server.
    ```
    bundle exec jekyll serve --watch
    ```
    Only include the `--watch` flag if you want Jekyll to watch for changes to the website’s files, such as you writing and saving a new blog post or webpage, and to include these changes on refreshing your web browser. 

6. To preview your site in your web browser, navigate to [http://localhost:4000](http://localhost:4000).


## How to deploy the MISP website

~~~
rake2.0 -f Rakefile generate
rake2.0 -f Rakefile publish
~~~


