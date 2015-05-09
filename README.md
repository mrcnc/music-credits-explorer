## Description
Find new music by searching through album and song credits.  This application is a mashup of the [Rovi Music API](http://prod-doc.rovicorp.com/mashery/index.php/Data/APIs/Rovi-Music) and the [EchoNest Artist API](http://developer.echonest.com/docs/v4/artist.html)

## Prerequisites
You will need to get [developer keys for Rovi](https://developers.rovicorp.com/GettingStarted) and an [API key from EchoNest](https://developer.echonest.com/account/register).  Then you need to set the following environment variables:
```
export ROVI_KEY="<your_rovi_application_key>"
export ROVI_SECRET="<your_rovi_application_secret>"
export ECHO_NEST_API_KEY="<your_echonest_api_key>"
```

Also, if you aren't using [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/), you should be.

## Installation


