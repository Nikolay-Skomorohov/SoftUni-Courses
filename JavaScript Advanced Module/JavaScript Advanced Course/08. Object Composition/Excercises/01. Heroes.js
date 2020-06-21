function solve() {
    function fighter(name) {
        let newFighter = {
            name,
            stamina: 100,
            health: 100,
            fight
        };
        function fight() {
            newFighter.stamina -= 1;
            console.log(`${newFighter.name} slashes at the foe!`);
        };
        return newFighter;
    };

    function mage(name) {
        let newMage = {
            name,
            health: 100,
            mana: 100,
            cast
            };
        function cast(spellName) {
            newMage.mana -= 1;
            console.log(`${newMage.name} cast ${spellName}`)
        };
        return newMage;
    };

    return {mage, fighter};
};

let create = solve();
const scorcher = create.mage("Scorcher");
scorcher.cast("fireball")
scorcher.cast("thunder")
scorcher.cast("light")

const scorcher2 = create.fighter("Scorcher 2");
scorcher2.fight()

console.log(scorcher2.stamina);
console.log(scorcher.mana);
