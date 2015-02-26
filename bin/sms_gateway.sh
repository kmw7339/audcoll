curl -X POST https://api.twilio.com/2010-04-01/Accounts/ACdb5a91d3339b21464aa520db3a44ffe4/SMS/Messages.json \
    -u ACdb5a91d3339b21464aa520db3a44ffe4:42bd73958d012a9055e23164bbe1c82d \
    --data-urlencode "From=+14844627867" \
    --data-urlencode "To=+12155184613" \
    --data-urlencode 'Body=sample message from caraud'

