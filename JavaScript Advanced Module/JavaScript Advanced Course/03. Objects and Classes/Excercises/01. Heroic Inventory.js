function solve(aList) {
    let result = [];
    for (let i = 0; i < aList.length; i++) {
           let heroData = aList[i].split(" / ");
           
           let heroObj = {"name":heroData[0], "level":Number(heroData[1])};
           if (heroData[2]) {
              let heroItems = heroData[2].split(", ");
              heroObj["items"] = heroItems;
           }
           else {
                  heroObj["items"] = [];
           }
           result.push(heroObj);
    }
    console.log(JSON.stringify(result));
}

solve(['Isacc / 25 / Apple, GravityGun', 
       'Derek / 12 / BarrelVest, DestructionSword', 
       'Hes / 1 / Desolator, Sentinel, Antara']);
solve(['Jake / 1000 / Gauss, HolidayGrenade']);