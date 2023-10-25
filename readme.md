# Environment Setup for Cooking
## Pre requsite
* Update the env.json file with your Editor Directory and Game Directory **Without trailing \\**

## Setting up
* Run `InitEnv -p <PluginName>`
* Validate all the files/folders in the base directory.

## Running cook command
* Run `1.<PluginName>-Cook.bat`
* wait for it to complete.
* Run `2-<PluginName>-Process-Package.bat`
* Validate `.pak` file in your game folder.

## Cleanup Environment
* Run `InitEnv -c` to cleanup all the files created for cooking the plugin.

## Simulating Time Table
* Modify the `3-<PluginName>-SimulateTimeTables.bat` with your timetable path and additional parameters. Refer [here](https://docs.google.com/document/d/1I6AABG0TIIS1Cg8ccXWzTYYGaO0qEKlRZkqkCABI1M0/edit#heading=h.wxcjlftbjprx) for the command.
* Run the `3-<PluginName>-SimulateTimeTables.bat`
* Validate time table has a valid data track in the editor.