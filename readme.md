Waffle House Order Logic System (Structure Only)
🍽️ Order Flow Structure
One ticket contains up to 5 seats (per table).
Orders are grouped by similar items.
Only one "Mark" call per ticket.
“Mark” is followed by number of plates first, then individual item details.
🔤 Naming Conventions
Platter = meat + eggs + grits + toast
Plate = item with added hashbrowns that do not usually come with them
Waffle plate = used for waffles or light items like toast & eggs
Bowl = either grits or hashbrowns in a bowl, layered with other ingredients
🔺 Mark
You said:
do up to 8 seats
ChatGPT said:
Understood. Here's the complete structure-only logic for your Waffle House order system, supporting up to 8 seats. This is concise, consistent, and formatted as a backend reference document (no pricing, no examples):
🧾 Waffle House Order System — Structure Logic (No Pricing)
🪑 Ticket & Table Logic
One ticket supports up to 8 seats per table.
Orders are grouped by shared attributes (eggs, waffles, etc.) to streamline Mark.
All plates must be assigned to a seat/person.
Call plates first in the Mark (e.g. platters, plates, waffle plates, bowls).
📦 Plate Types
Platter = meat + eggs + grits + toast (white toast implied)
Plate = item with added hashbrowns that do not normally include them
Waffle plate = for waffles or standalone light items (e.g. eggs + toast)
Sandwich plate = sandwich with added hashbrowns
Bowl = grits or hashbrowns layered with other items
🔤 Toast & Sides
White toast is default; only call toast if non-white or unbuttered.
Grits are implied on platters; only called if modified (e.g. cheese grits).
Cheese grits or no grits must be explicitly marked.
Sandwiches do not include grits or hashbrowns unless called as a plate.
🍳 Eggs
Single = 1 egg
Order = 2 eggs
Triple = 3 eggs
Egg doneness must always be called (e.g. scrambled, over light, etc).
Modifiers (e.g. with cheese) must be marked.
🟨 Pull
Pull is only for meats and proteins (except diced ham).
Always call meat by full name: bacon, sausage, pork chop, chicken, etc.
Include doneness if relevant (e.g. rare steak, crispy bacon).
“½” portions must be used when required (e.g. ½ bacon for biscuit).
“Two halves” = two separate ½ portions for two items.
Pre-diced ham does not get pulled.
Cheesesteak must be pulled (even in omelets or melts).
Sausage and sausage for sandwich are distinct items.
Pulls are grouped and called across the entire ticket.
🟩 Drop
Drop is only for hashbrowns (never grits, eggs, or waffles).
Use quantity: Drop 1, Drop 2, etc.
Always call style (e.g. scattered).
Do not say "bowl" in the drop — only call number of orders.
Drop hashbrowns if:
It’s a plate
It’s a dinner substitution
It’s a hashbrown bowl
🟥 Mark
“Mark” is called once per ticket.
Begin with number and type of plates (e.g. Mark 3 platters, 1 plate, 2 waffle plates…).
All egg orders must specify count and doneness.
Grits or toast modifications must be included if different from default.
Cheese or other modifiers must be included.
Bowls must be described (e.g. hashbrown bowl, grits bowl) and list ingredients in order (meat, cheese, egg).
Use "on" when a set of items share a style but differ in one modifier.
Use "like" when two or more items go on the same plate.
