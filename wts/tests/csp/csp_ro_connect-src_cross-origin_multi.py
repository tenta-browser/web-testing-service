def main(request, response):
    import simplejson as json
    f = file('config.json')
    source = f.read()
    s = json.JSONDecoder().decode(source)
    url1 = "http://" + s['host'] + ":" + str(s['ports']['http'][1])
    url2 = "http://" + s['host'] + ":" + str(s['ports']['http'][0])
    _CSP = "connect-src http://www.w3.org https://www.tizen.org; script-src 'self' 'unsafe-inline'"
    response.headers.set("Content-Security-Policy", _CSP)
    response.headers.set("X-Content-Security-Policy", _CSP)
    response.headers.set("X-WebKit-CSP", _CSP)
    return """<!DOCTYPE html>
<!--
Copyright (c) 2013 Samsung Electronics Co., Ltd.

Licensed under the Apache License, Version 2.0 (the License);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Authors:
        Ran, Wang <ran22.wang@samsung.com>
-->

<html>
  <head>
    <title>CSP Test: csp_ro_connect-src_cross-origin_multi_xmlhttprequest</title>
    <link rel="author" title="Samsung" href="http://www.Samsung.com"/>
    <link rel="help" href="http://www.w3.org/TR/2012/CR-CSP-20121115/#connect-src"/>
    <meta name="flags" content=""/>
    <meta name="assert" content="connect-src http://www.w3.org https://www.tizen.org"/>
    <meta charset="utf-8"/>
    <script src="../resources/testharness.js"></script>
    <script src="../resources/testharnessreport.js"></script>
  </head>
  <body>
    <div id="log"></div>
    <script>
        var xhr = new XMLHttpRequest();

        test(function() {
            try {
                xhr.open("GET", "http://www.w3.org");
            } catch(e) {
                assert_unreached("Should not reach here, exception: " + e.message);
            }
        }, document.title + "_allowed_one");

        test(function() {
            try {
                xhr.open("GET", "https://www.tizen.org");
            } catch(e) {
                assert_unreached("Should not reach here, exception: " + e.message);
            }
        }, document.title + "_allowed_two");

        test(function() {
            try {
                xhr.open("GET", "http://www.google.com");
              } catch(e) {
                assert_unreached("Should not reach here, exception: " + e.message);
            }
        }, document.title + "_blocked");

        test(function() {
            try {
                xhr.open("GET", "support/csp.js");
            } catch(e) {
              assert_unreached("Should not reach here, exception: " + e.message);
            }
        }, document.title + "_blocked_int");
    </script>
  </body>
</html>"""
