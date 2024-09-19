# The NanoBot Library

The NanoBot Program Library simulates actions taken by theoretical nanobots, to
prove the capabilities possible from years of research. It is made up of modules
and files with distinct purposes. The former being to replicate the scanning and 
searching of specific cells of the human body. The latar is to showcase the 
nanbot's ability to mimic antigens of cells to circumvent the attacking T-cells.

## Table of contents

- Requirements
- Installation
- Configuration
- Maintainers

## Requirements

This Library requires the following modules:

- [Moving Toward Target](MovingTowardTarget/MainFile.py)
- [AntigenRPG](AntigenRPG/MainFile.py)

## Installation

The required modules do not need external installs of python libraries through pip.
The only requirement is to run the MainFile of respective modules with their python
files within the same directory. All other files will not run, as they are missing
the validation to check whether it was the __main__ file.

## Configuration

1. Go to AntigenRPG/MovingTowardTarget (directories) » SettingsFile
2. Edit/change desired constant/attribute, for example "NANOBOT_NUMBER"
3. Save and reload entire directory to see effects of changes

The library has modifiable SettingsFiles within respective modules.
Documentation is available per SettingsFile for what each constant/attribute
affects.

## Maintainers

- Imran Almashoor
