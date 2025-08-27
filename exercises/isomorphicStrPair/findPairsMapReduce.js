#!/usr/bin/env node

function isoPairs(wordlist) {

    function mapWord(word){
        charCount=0;
        charDict = {};
        output='';
        for (c of word){
            if (!(c in charDict)){
                charDict[c]=String.fromCharCode(charCount)
                charCount+=1
            }
            output+=charDict[c]
        }
        return output
    }
    initial={}
    initial[0]=0
    pairCount=wordlist.map(mapWord).reduce((accumulator, currentval) => {
        if (currentval in accumulator){
            accumulator[0]+=accumulator[currentval]
            accumulator[currentval]+=1
        } else {
            accumulator[currentval]=1
        }
        return accumulator
    },initial)
    
    return pairCount[0]
    }


console.log(isoPairs(['egg','foo','bar']))
console.log(isoPairs(['egg','foo','bar','paper','title']))
console.log(isoPairs(['egg','foo','bar','paper','title','add','taa']))

function main() {
const arrOfStrings = process.argv.slice(2);
output = isoPairs(arrOfStrings);
console.log(output)
}



if (require.main === module) {
  main();
}

module.exports = { isoPairs };