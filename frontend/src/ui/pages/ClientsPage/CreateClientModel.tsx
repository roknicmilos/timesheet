import Modal from "react-modal";
import ClientForm from "./ClientForm";

interface CreateClientModalProps {
    isOpen: boolean;
    onSubmit(): void;
    onClose(): void;
}

const modalStyles = {
    content: {
        top: "50%",
        left: "50%",
        right: "auto",
        bottom: "auto",
        marginRight: "-50%",
        transform: "translate(-50%, -50%)",
        borderRadius: "10px",
        padding: 0,
    },
    overlay: {
        backgroundColor: "rgba(0, 0, 0, 0.8)",
        padding: 0,
    },
};

export default function CreateClientModal({ isOpen, onSubmit, onClose }: CreateClientModalProps) {
    return (
        <Modal isOpen={isOpen} style={modalStyles} ariaHideApp={false}>
            <div className="modal__content">
                <h2 className="heading">Create new client</h2>
                <div className="modal__close" onClick={onClose}>
                    <span className="modal__icon"></span>
                </div>
                <ClientForm onSubmit={onSubmit} isInModal={true} />
            </div>
        </Modal>
    );
}
