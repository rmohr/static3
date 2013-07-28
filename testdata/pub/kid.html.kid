<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" 
    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" 
      xmlns:py="http://purl.org/kid/ns#" 
      xml:lang="en">
  <head>
    <title>kid magic test</title>
    <style type="text/css">
table.wsgivars {
    background-color: #ddd;
    border: solid 1px #777;
    width: 600px%
}
table.wsgivars  td {
    background-color: #fff;
}
    </style>
  </head>
  <body>
    <h1>Title: $title</h1>
    <p>
        If everything is working, the title above should be: "Kid Test" 
        and below you should see a table of your WSGI environ.
        You should receive no 304s from this resource.
    </p>
    <table class="wsgivars">
      <caption>varables longer than 50 characters truncated</caption>
      <tr><th>Variable</th><th>Value</th></tr>
      <tr py:for="k, v in environ.iteritems()">
        <td py:content="k"/>
        <td py:content="str(v)[:50]"/>
      </tr>
    </table>
  </body>
</html>
