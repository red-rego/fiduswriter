import {Plugin} from "prosemirror-state"

export const icon = (text, name) => {
    let span = document.createElement("span")
    span.className = "menuicon " + text
    span.title = name
    span.textContent = text
    span.setAttribute('data-type', text)
    return span
}

class SelectionSizeTooltip {
    constructor(view) {
        this.update(view, null)
    }

    update(view, lastState) {
        if (view.state) {
            const storedMarks = view.state.storedMarks || view.state.selection.$head.marks()
            if (storedMarks) {
                for (let mark of storedMarks) {
                    console.log(mark.type)
                }
            }
        }
    }
}

class MenuView {
    constructor(items, view) {
        this.items = items
        this.editorView = view

        this.dom = document.createElement("div")
        this.dom.className = "inline-tools"
        items.forEach(({dom}) => this.dom.appendChild(dom))

        this.dom.addEventListener("mousedown", e => {
            e.preventDefault()
            view.focus()
            items.forEach(({command, dom}) => {
                if (dom.contains(e.target))
                    command(view.state, view.dispatch, view)
            })
        })

        this.update(view)
    }

    update(view) {
        let active_marks = []

        if (view.state) {
            const storedMarks = view.state.storedMarks || view.state.selection.$head.marks()
            if (storedMarks) {
                for (let mark of storedMarks) {
                    active_marks[mark.type.name] = true
                }
            }
        }

        this.items.forEach(({command, dom}) => {
            if (active_marks[dom.getAttribute('data-type')]) {
                dom.classList.add('active')
            } else {
                dom.classList.remove('active')
            }
        })
    }

    destroy() { this.dom.remove() }
}

export const InlineTools = (tools) => {
    return new Plugin({
        view(view) {
            let menuView = new MenuView(tools, view)
            view.dom.parentNode.appendChild(menuView.dom)
            return menuView
        }
    })
}
