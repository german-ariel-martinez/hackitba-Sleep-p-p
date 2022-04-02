import Vue, { VNode, CreateElement, RenderContext } from "vue";
const SIZE = {
    small: "16px",
    default: "24px",
    medium: "28px",
    large: "36px"
};

export default Vue.component(
    "md-icon",
    {
        props: {
            large: Boolean,
            medium: Boolean,
            small: Boolean
        },
        functional: true,
        render(createElement: CreateElement, context: RenderContext): VNode {
            let fontSize = SIZE.default;
            const props = context.props;
            const data = context.data;
            const children = context.children || [];
            switch (true) {
                case props.small:
                    fontSize = SIZE.small;
                    break;
                case props.medium:
                    fontSize = SIZE.medium;
                    break;
                case props.large:
                    fontSize = SIZE.large;
                    break;
            }
            data.style = { fontSize, ...data.style };
            data.staticClass = "material-icons md-icon";
            return createElement("i", data, children);
        }
    });
