---
title: MISP OpenAPI spec
permalink: /documentation/openapi
type: full 
toc: false
aliases:
    - /documentation/openapi.html
---

# MISP OpenAPI specification

Browse the MISP Automation API below, or [view the OpenAPI YAML specification](https://raw.githubusercontent.com/MISP/MISP/develop/app/webroot/doc/openapi.yaml) directly.

<redoc></redoc>
<!-- Pin Redoc 2: Redoc 3's module bundle cannot be loaded as a classic script. -->
<script src="https://cdn.redocly.com/redoc/v2.5.1/bundles/redoc.standalone.js"></script>
<script>
Redoc.init(
    'https://raw.githubusercontent.com/MISP/MISP/develop/app/webroot/doc/openapi.yaml',
    {
        // Recheck the sticky header height after viewport changes as well.
        scrollYOffset: function () {
            var header = document.querySelector('.navbar-affixed-top');
            return header ? header.getBoundingClientRect().height : 0;
        }
    },
    document.querySelector('redoc')
);
</script>
