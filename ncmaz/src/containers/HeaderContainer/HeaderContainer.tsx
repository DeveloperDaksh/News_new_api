import Header from "components/Header/Header";
import React, { FC } from "react";
import { useAppSelector } from "app/hooks";
import { selectCurrentPageData } from "app/pages/pages";

export interface HeaderContainerProps {
  className?: string;
}

const HeaderContainer: FC<HeaderContainerProps> = ({ className = "" }) => {
  const currentPage = useAppSelector(selectCurrentPageData);

  return <Header currentPage={currentPage} />;
};

export default HeaderContainer;
