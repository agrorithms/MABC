#!/usr/bin/env node
//as loopin through, add n-1 for the count at the time?
function countIsoStrPairs(strArr) {
    freqStrNum = {}
    pairCount = 0

    for (const word of strArr){
        isomorphicArr=[];
        charToNum={};
        charCount=0;
        for (let j = 0; j < word.length; ++j){
            if (!(word[j] in charToNum)){
                charToNum[word[j]]=charCount
                charCount+=1
            }
            isomorphicArr.push(charToNum[word[j]])
        }
        if (!(isomorphicArr in freqStrNum)){
            freqStrNum[isomorphicArr]=1
        } else {
            pairCount+=freqStrNum[isomorphicArr]
            freqStrNum[isomorphicArr]+=1
        }


    }
    return pairCount

}


function main() {
const arrOfStrings = process.argv.slice(2);
output = countIsoStrPairs(arrOfStrings);
console.log(output)
}



if (require.main === module) {
  main();
}

module.exports = { countIsoStrPairs };
