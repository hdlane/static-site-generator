# Static Site Generator

## Description

Static site generator built from scratch with Python which parses markdown to generate HTML pages.

<p align="center">
<img src="https://github.com/user-attachments/assets/56e5d4ff-921d-43b3-bfe1-268d14dc2cf3" />
</p>

### Features

* Takes Markdown (.md) files and converts them to HTML pages
* Handles almost all the [Basic Syntax](https://www.markdownguide.org/cheat-sheet/#basic-syntax) of Markdown (excepth Horizontal Rule)
* Store images, css, and JavaScript files in the static folder to use across pages
* Uses template file to give consistency to each generated page

## Installation

### Requirements

* Python 3.6+
* Linux or MacOS to natively run the shell scripts (.sh)

## Usage

### Getting Started

* Clone the repo `https://github.com/hdlane/static-site-generator.git` and `cd` into it, then set the proper permissions for the scripts

```
git clone https://github.com/hdlane/static-site-generator.git
cd 'static-site-generator'
chmod +x main.sh test.sh
```

* Create Markdown files and save them in the `content/` folder. File names will be in the URL. 
* Create subfolders to make subpages. If you make a file `index.md` for a folder, it can be navigated to without including the file name (http://localhost:8888/blog)
* Save images, css, and JavaScript files in the `static/` folder
* It is required that each Markdown file begin with an `h1` tag: `# Title`
* At the root of the project, run `./main.sh` to begin generating the pages
* Navigate to http://localhost:8888/ to view the site

### Using Markdown

Markdown (.md) files are created in any text editor. Use the [Getting Started](https://www.markdownguide.org/getting-started/) guide to learn how to use Markdown.

### Saving Markdown

When the Markdown file is created, save it to the `content/` folder at the root of the project. When the files are generated, they will be pulled from that folder.

### Starting The Server

The server can be started by running the `./main.sh` file at the root of the project. That will kick off a process that cleans up the `public/` folder, copies over the `static/` folder and its files/folders, and then generates the HTML pages. 

## License

[MIT](https://choosealicense.com/licenses/mit/)
