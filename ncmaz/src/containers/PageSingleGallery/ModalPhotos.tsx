import React, { FC, Fragment, useEffect, useState } from "react";
import { Dialog, Transition } from "@headlessui/react";
import NextPrev from "components/NextPrev/NextPrev";
import ButtonClose from "components/ButtonClose/ButtonClose";

export interface ModalPhotosProps {
  imgs: string[];
  onClose: () => void;
  isOpen: boolean;
  initFocus?: number;
}

const ModalPhotos: FC<ModalPhotosProps> = ({
  imgs,
  isOpen,
  onClose,
  initFocus = 0,
}) => {
  const [indexActive, setindexActive] = useState(initFocus);

  useEffect(() => {
    setindexActive(initFocus);
  }, [initFocus]);

  const handleClickNext = () => {
    if (indexActive >= imgs.length - 1) {
      return setindexActive(() => 0);
    }
    setindexActive((i) => i + 1);
  };

  const handleClickPrev = () => {
    if (indexActive <= 0) {
      return setindexActive(() => imgs.length - 1);
    }
    setindexActive((i) => i - 1);
  };

  const renderModalPhotos = () => {
    return (
      <Transition
        appear
        enter="ease-out duration-300"
        enterFrom="opacity-0"
        enterTo="opacity-100"
        leave="ease-in duration-200"
        leaveFrom="opacity-100"
        leaveTo="opacity-0"
        show={isOpen}
        as={Fragment}
      >
        <Dialog
          as="div"
          className="fixed inset-0 z-50 overflow-y-auto"
          onClose={onClose}
        >
          <div className="min-h-screen px-4 text-center">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0"
              enterTo="opacity-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100"
              leaveTo="opacity-0"
            >
              <Dialog.Overlay className="fixed inset-0 bg-white dark:bg-neutral-800" />
            </Transition.Child>
            <div className="absolute left-2 top-2 md:top-4 md:left-4">
              <ButtonClose
                iconSize="w-6 h-6"
                className=" w-11 h-11"
                onClick={onClose}
              />
            </div>
            {/* This element is to trick the browser into centering the modal contents. */}
            <span
              className="inline-block h-screen align-middle"
              aria-hidden="true"
            >
              &#8203;
            </span>

            <div className="relative inline-block w-full max-w-5xl my-8 align-middle ">
              <img
                className="rounded-lg mx-auto max-h-screen  "
                src={imgs[indexActive]}
                alt="abc"
              />
              <NextPrev
                onClickNext={handleClickNext}
                onClickPrev={handleClickPrev}
                containerClassName="absolute -inset-x-0 xl:-inset-x-14 2xl:-inset-x-20 top-1/2 transform -translate-y-1/2 flex justify-between"
              />
            </div>
          </div>
        </Dialog>
      </Transition>
    );
  };

  return renderModalPhotos();
};

export default ModalPhotos;
