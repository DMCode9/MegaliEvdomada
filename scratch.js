const text = "Ὁ ὑψωθεὶς ἐν τῷ Σταυρῷ ἑκουσίως, τῇ ἐπωνύμῳ Σου καινῇ";
const glossaryData = {
    "τῇ ἐπωνύμῳ Σου": "σε αυτήν που φέρει το όνομά Σου",
    "ἐπωνύμῳ": "που φέρει το όνομά σου",
    "Σταυρῷ": "Σταυρό"
};
let sortedGlossaryKeys = Object.keys(glossaryData).sort((a,b) => b.length - a.length);

const escapeRegExp = string => string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const pattern = sortedGlossaryKeys.map(escapeRegExp).join('|');
const glossaryRegex = new RegExp(`(${pattern})`, 'g');

const isGrk = (c) => /[\u0370-\u037D\u037F-\u0386\u0388-\u03FF\u1F00-\u1FFF]/.test(c);

const parts = text.split(/(<[^>]+>)/g);
for(let i=0; i<parts.length; i++) {
    if(i % 2 === 0) {
        parts[i] = parts[i].replace(glossaryRegex, (match, p1, offset, string) => {
            const before = offset === 0 ? '' : string[offset - 1];
            const after = offset + match.length === string.length ? '' : string[offset + match.length];
            if (!isGrk(before) && !isGrk(after)) {
                const def = glossaryData[match].replace(/"/g, '&quot;');
                return `<span class="glossary-term" data-term="${match}" data-def="${def}">${match}</span>`;
            }
            return match;
        });
    }
}
console.log(parts.join(''));
