from graphviz import Digraph

f = Digraph(format='png', name='stack')
f.attr(rankdir='TB', size='8')

f.attr('node', shape='plaintext')
f.node('p0', "<<table><tr><td>   </td></tr><tr><td>   </td></tr><tr><td>   </td></tr></table>>")

f.node('p1', "<<table><tr><td>+</td></tr><tr><td>2</td></tr><tr><td>3</td></tr></table>>")
f.node('p2', "<<table><tr><td>+</td></tr><tr><td>2</td></tr><tr><td>3</td></tr></table>>")
f.node('p3', "<<table><tr><td>+</td></tr><tr><td>2</td></tr><tr><td>3</td></tr></table>>")
f.node('p4', "<<table><tr><td>+</td></tr><tr><td>2</td></tr><tr><td>3</td></tr></table>>")

f.view()
