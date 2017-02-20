## chapter 1. introduction 
* examle of using `BeautifulSoup`:
```python
bsObj = BeautifulSoup(htmlStr)
print(bsObj.h1)
```
* in fact, any of the following function calls would produce the same output:
```python
bsObj.html.body.h1
bsObj.body.h1
bsObj.html.h1
```
* we may also get dictionary of attributes or access individual attribute:
```python
myTag.attrs
myImgTag.attrs['src'] # or even myImgTag['src'] see [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes)
```
## chapter 2. html parsing
### types of objects in `BeautifulSoup`
*`BeautifulSoup` objects: Seen in previous code examples as `bsObj`
* `Tag objects`: Retrieved in lists or individually by calling `find()` and `findAll()` on a `BeautifulSoup` object
* `NavigableString` objects: Used to represent text within tags, rather than the tags themselves (some functions operate on, and produce, `NavigableStrings`, rather than tag objects).
* Comment object: Used to find HTML comments in comment tags, `<!--like this one-->`.
-----
* we may also get text from an object:
```python
nameList = bsObj.findAll("span", {"class":"green", "class":"red"}) 
for name in nameList:
    print(name.get_text())
```
### `find()` and `findAll()`
* main functions to use - find() and findAll(); we provide tag (or list of tags) and attributes (or list of attributes, in this case we have **or** filter):
```python
.findAll("span", {"class":"green", "class":"red"})
```
* it seems we can provide actual list - see [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters);
### navigating trees
* we can navigate children(descendants), siblings and parents (the last one is rare):
```python
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
```
### regular expressions
* we may use regular expressions (it seems we have to wrap them into `re.compile()` - see [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-regular-expression)):
```python
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")}) for image in images:
    print(image["src"])
```
### lambda function
* BeautifulSoup allows us to pass certain types of functions as parameters into the fin dAll function. The only restriction is that these functions must take a tag object as an argument and return a boolean. Every tag object that BeautifulSoup encounters is evaluated in this function, and tags that evaluate to “true” are returned while the rest are discarded.
```pyhton
soup.findAll(lambda tag: len(tag.attrs) == 2)
```
```html
<div class="body" id="content"></div>
<span style="color:red" class="title"></span>
```













