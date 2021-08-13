# Torrent Leecher
### Moded By <a href='https://youtube.com/channel/UCXl_dzFIxfmAlaPtD7AZY7A'>𝕎𝕆𝕃𝕋ℝ𝔼𝕏</a>

- This Bot allows you to leech (re-upload) contents from internet including torrent to telegram.

###  Features

* Set as Private (using password)
* Able to use at group
* Able to leech larger than 2GB (telegram max upload at once)
* Split as video (.mp4, .mkv, .avi, .webm, .wmv, .mov)
* Upload files as media or as document
* Upload files as a single zip file
* Custom thumbnail
* Default torrent tracker
* Customizeable language (default is english)
* Configuration using environment variable

## Configuration

Change config by set the corresponding environment variable name.

* `WORKDIR` : working directory path
* `LOG_FILE` : log file name
* `MAX_LOG_SIZE` : maximum log size
* `EDIT_SLEEP` : delay between edit message
* `UPLOAD_MAX_SIZE` : maximum file size (in bytes) upload at once (watchout telegram max upload size)
* `UPLOAD_AS_DOC` : upload any files as document (1 or 0)
* `UPLOAD_AS_ZIP` : upload any files as a bundled zip file (1 or 0)
* `ARIA2_DIR` : download directory before uploading
* `TORRENT_TRACKER` : addition tracker for all torrent, separated by (`,`)
* `BAR_SIZE` : bar size on upload and download
* `THUMBNAIL_NAME` : default thumbnail file name
* `LOCAL` : languange bot using
* `CHAT_ID` : default chat_ids that have access to bot, separated by (`,`)

## Deploy button

<p><a href="https://heroku.com/deploy"> <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" /></a></p>

### Credits:
- [Azamaulanaa](https://github.com/azamaulanaaa/botkaca) For Main Repo.
