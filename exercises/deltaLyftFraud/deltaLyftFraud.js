#!/usr/bin/env node

function deltaLyftFraudCheck(deltaUsers, lyftUsers, integratedUsers) {
    const deltaSet= new Set(deltaUsers)
    const lyftSet = new Set(lyftUsers)
    const integratedSet = new Set(integratedUsers)

    differenceUsers = deltaSet.symmetricDifference(lyftSet);
    fraudUsers=differenceUsers.intersection(integratedSet);
    console.log(integratedSet.difference(deltaSet.union(lyftSet)));
    fraudUsers=fraudUsers.union(integratedSet.difference(deltaSet.union(lyftSet)));

    fraudUsers=Array.from(fraudUsers);
    fraudUsers.sort();

    return fraudUsers

}


function main() {
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error("Error: Provide 3 arguments (comma-separated lists).");
  process.exit(1);
}

const lists = args.map(arg => arg.split(','));
output = deltaLyftFraudCheck(lists[0],lists[1],lists[2]);
console.log(output)
}



if (require.main === module) {
  main();
}

module.exports = { deltaLyftFraudCheck };
