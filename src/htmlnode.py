class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children=None, props=None)

        if self.children != None:
            raise Exception("LeafNode shouldn't have children")
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have value")
        
        if self.tag == None:
            return self.value
        
        if self.tag == "p":
            return f"<p>{self.value}</p>"
        elif self.tag == "b":
            return f"<b>{self.value}</b>"
        elif self.tag == "i":
            return f"<i>{self.value}</i>"
        elif self.tag == "code":
            return f"<code>{self.value}</code>"
        elif self.tag == "a":
            return f"<a href=\"{self.prop["href"]}\">{self.value}</a>"
        elif self.tag == "img":
            return f"<img src=\"{self.prop["src"]}\">"
        else:
            raise ValueError("not a tag")

        