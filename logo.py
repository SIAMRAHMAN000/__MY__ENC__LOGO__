
#Encoding password
import base64
from pyfiglet import Figlet
skill = Figlet(font='standard')
siam = skill.renderText('SIAM')
 
siamlenc=base64.b64encode(siam.encode("ascii","strict"))  
 

import base64
#Your credentials that you want to protect
siaml = "IF9fX18gX19fICAgIF8gICAgX18gIF9fICAgX19fXyAgXyAgIF8gX19fIF9fX18gIF8gICBfIF9fX19fIF9fX18gIAovIF9fX3xfIF98ICAvIFwgIHwgIFwvICB8IHwgIF8gXHwgfCB8IHxfIF8vIF9fX3x8IHwgfCB8IF9fX198ICBfIFwgClxfX18gXHwgfCAgLyBfIFwgfCB8XC98IHwgfCB8XykgfCB8X3wgfHwgfFxfX18gXHwgfF98IHwgIF98IHwgfF8pIHwKIF9fXykgfCB8IC8gX19fIFx8IHwgIHwgfCB8ICBfXy98ICBfICB8fCB8IF9fXykgfCAgXyAgfCB8X19ffCAgXyA8IAp8X19fXy9fX18vXy8gICBcX1xffCAgfF98IHxffCAgIHxffCB8X3xfX198X19fXy98X3wgfF98X19fX198X3wgXF9cCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAK=="
 
#decode a message
msg=base64.b64decode(password)
decoded_value=msg.decode('ascii','strict')
 
#display the decoded value on a screen
print(decoded_value)
