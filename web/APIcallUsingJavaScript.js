fetch('https://pokeapi.co/api/v2/pokemon/pikachu')
    .then(res => res.json())
    .then(data => {
        console.log('name: ' + data.name);
        console.log('pokemon type: ' + data.types.map(type => type.type.name));
        console.log('abilities: ' + data.abilities.map(ability => ability.ability.name).join(', '));
    });