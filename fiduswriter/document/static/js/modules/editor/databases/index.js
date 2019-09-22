import {ModImageDB} from "./images"
import {ModBibliographyDB} from "./bibliography"
import {ModFileDB} from "./files"


export class ModDB {
    constructor(editor) {
        editor.mod.db = this
        this.editor = editor
        console.log("this.editor.mod ", this.editor.mod)
        new ModImageDB(this)
        new ModBibliographyDB(this)
        new ModFileDB(this)

    }

    // remove images/citation items that are no longer part of the document.
    clean() {
        const usedImages = [],
            usedBibs = []
            console.log("this.editor.view.state.doc -", this.editor.view.state.doc.descendants(node =>{console.log("node :- ", node)}))

        this.editor.view.state.doc.descendants(node => {
            if (node.type.name==='citation') {
                node.attrs.references.forEach(ref => usedBibs.push(parseInt(ref.id)))
            } else if (node.type.name==='figure' && node.attrs.image) {
                usedImages.push(node.attrs.image)
            }
        })

        this.editor.mod.footnotes.fnEditor.view.state.doc.descendants(node => {
            if (node.type.name==='citation') {
                node.attrs.references.forEach(ref => usedBibs.push(parseInt(ref.id)))
            } else if (node.type.name==='figure' && node.attrs.image) {
                usedImages.push(node.attrs.image)
            }
        })

        const unusedImages = Object.keys(this.imageDB.db).filter(value =>
                !usedImages.includes(parseInt(value))
            ),
            unusedBibs = Object.keys(this.bibDB.db).filter(value =>
                !usedBibs.includes(parseInt(value))
            )
        unusedImages.forEach(id => this.imageDB.deleteImage(id))
        unusedBibs.forEach(id => this.bibDB.deleteReference(id))
    }
}
