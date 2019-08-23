export function extractTemplate(doc) {
    const template = JSON.parse(JSON.stringify(doc))
    // Set attributes to default values
    delete template.attrs.citationstyle
    delete template.attrs.documentstyle
    delete template.attrs.tracked
    template.attrs.language = template.attrs.languages[0]
    template.attrs.papersize = template.attrs.papersizes[0]
    template.content = template.content.filter(part => !part.attrs || !part.attrs.deleted)
    template.content.forEach(part => {
        delete part.content
        if (part.type==='title') {
            delete part.attrs
            return
        } else if (part.attrs.initial) {
            part.content = JSON.parse(JSON.stringify(part.attrs.initial))
        } else if (['heading_part', 'richtext_part', 'file_upload_part'].includes(part.type)) {
            part.content = [{type: part.attrs.elements[0]}]
        } else if (part.type==='table') {
            part.content = [{type: 'table', content: [{type: 'table_row', content: [{type: 'table_cell', content: [{type: 'paragraph'}]}]}]}]
        }
        delete part.attrs.deleted
        if (!part.attrs.help) {
            delete part.attrs.help
        }
        if (!part.attrs.language) {
            delete part.attrs.language
        }
        if (!part.attrs.locking) {
            delete part.attrs.locking
        }
        if (!part.attrs.initial) {
            delete part.attrs.initial
        }
        if (!part.attrs.metadata) {
            delete part.attrs.metadata
        }
        delete part.attrs.hidden
        if (part.attrs.optional === 'hidden') {
            part.attrs.hidden = true
        }
        if (!part.attrs.optional) {
            delete part.attrs.optional
        }
    })
    return template

}
