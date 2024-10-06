// https://leetcode.cn/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150

function fullJustify(words: string[], maxWidth: number): string[] {
    const res: string[] = [];
    const space = ' ';
    let curLine: string[] = [];
    let curLen = 0;
    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        if (curLen + word.length + curLine.length <= maxWidth) {
            curLine.push(word);
            curLen += word.length;
        } else {
            let spaceNum = maxWidth - curLen;
            let extraSpace = spaceNum % (curLine.length - 1);
            const avgSpace = Math.floor(spaceNum / (curLine.length - 1));
            let theLine = "";
            for (let j = 0; j < curLine.length; j++) {
                theLine += curLine[j];
                if (j != (curLine.length - 1)) {
                    if (extraSpace > 0) {
                        theLine += space;
                        extraSpace--;
                    }
                    theLine += space.repeat(avgSpace);
                } else if (curLine.length === 1) {
                    // edge case: 一行一个单词，且长度不等于 maxWidth
                    theLine += space.repeat(maxWidth - curLen);
                }
            }
            res.push(theLine);
            curLine = [word];
            curLen = word.length;
        }
    }
    if (curLine.length > 0) {
        res.push(curLine.join(space).padEnd(maxWidth, space));
    }
    return res;
};


// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    {
        words: ["This", "is", "an", "example", "of", "text", "justification."], maxWidth: 16, result: ["This    is    an", "example  of text", "justification.  "]
    },
    {
        words: ["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth: 16, result: ["What   must   be", "acknowledgment  ", "shall be        "]
    },
    {
        words: ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth: 20, result: ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "]
    }
];

describe.each(testcases)(`words: $words, maxWidth: $maxWidth`, ({ words, maxWidth, result }) => {
    test(`returns ${result}`, () => {
        const whatyougot = fullJustify(words, maxWidth);
        expect(whatyougot).toEqual(result);
    });
});
