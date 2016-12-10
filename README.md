# SublimeEsaIo

A [Sublime Text 3](http://www.sublimetext.com/) plugin for [esa.io](https://esa.io/).

## Installation

### Manual installation

1. Find "Package Control: Add Repository" in Command Pallete.
2. Input "https://github.com/Satoh-D/SublimeEsaIo".
3. Find "Package Control: Install Package" in Command Pallete.
4. Select "SublimeEsaIo".

## Generating Access Token

you can generate API Access Tokens via the Web UI.

### Web UI

- Account -> Applications(https://[team].esa.io/user/applications)
- Personal access tokens -> Generate new token
- "Token description" you should give it a meaningful name, Example: for sublime esa
- "Select scopes" check both "Read" and "Write"
- click "Save" button

Paste the token in the settings section under the token option.


## Options

- `"token": ""`

  You must enter your Esa.io token here.

- `"team": ""`

  You must enter your joining team here.


## Usage

All functionality of the plugin is available in the command pallette.

### Creating Document(Save as WIP / Ship It!)

Use the `SublimeEsaIo` / `EsaIo` or `SublimeEsaIo` / `EsaIoShip` commands.  
A EsaIo will be created with contents of current file, URL of that document will be copied to the clipboard.


## Feature

- Edit document.
- Delete document.
- Convert Status (WIP -> Shipped / Shipped -> WIP).
- Multiple team (current single team only).

etc...


## License

MIT.


## Author

2016, [Sato Daiki](http://satoh-d.hatenablog.com/)  

- Blog: [http://satoh-d.hatenablog.com/](http://satoh-d.hatenablog.com/)  
- Twitter: [@Satoh_D](https://twitter.com/Satoh_D)
