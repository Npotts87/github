
var eeyore = { character: "Eeyore" };
var heffalumps = { character: "Heffalups" };
var kanga = { character: "Kanga" };
var christopher = { character: "Christopher" };
var pooh = { character: "Pooh" };
var tigger = { character: "Tigger" };
var owl = { character: "Owl" };
var piglet = { character: "Piglet" };
var rabbit = { character: "Rabbit" };
var gopher = { character: "Gopher" };
var bees = { character: "Bees" };

heffalumps.west = eeyore;

eeyore.east = heffalumps;
eeyore.south = kanga;

kanga.north = eeyore;
kanga.south = christopher;

christopher.west = owl;
christopher.east = rabbit;
christopher.north = kanga;
christopher.south = pooh;

owl.east = christopher;
owl.south = piglet;

rabbit.west = christopher;
rabbit.east = gopher;
rabbit.south = bees;

gopher.west = rabbit;

pooh.west = piglet;
pooh.north = christopher;
pooh.east = bees;
pooh.south = tigger;

piglet.north = owl;
piglet.east = pooh;

bees.west = pooh;
bees.north = rabbit;

tigger.north = pooh;

var player = {
    location: tigger
}

function move(direction) {
    if (player.location[direction] === undefined) {
        return "You cannot go " + direction;
    }else {
        player.location = player.location[direction];
        return "You are now at " + player.location.character + "house";
    }
}
console.log(move("north"));
console.log(move("north"));
console.log(move("east"));
console.log(move("east"));
console.log(move("east"));
