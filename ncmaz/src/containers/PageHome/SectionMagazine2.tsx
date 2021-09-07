import React, { FC, useState } from "react";
import Card2 from "components/Card2/Card2";
import { SectionMagazine1Props } from "./SectionMagazine1";
import HeaderFilter from "./HeaderFilter";
import useDemoTabFilter from "hooks/useDemoTabFilter";
import Card11 from "components/Card11/Card11";

export interface SectionMagazine2Props extends SectionMagazine1Props {}

const SectionMagazine2: FC<SectionMagazine2Props> = ({
  posts,
  tabs,
  heading = "🎈 Latest Articles",
}) => {
  let timeOut: NodeJS.Timeout | null = null;

  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [tabActive, setTabActive] = useState<string>(tabs[0]);

  const activePosts = useDemoTabFilter({
    isLoading,
    initPosts: posts,
    tabs,
    tabActive,
  });

  const handleClickTab = (item: string) => {
    if (item === tabActive) {
      return;
    }
    setIsLoading(true);
    setTabActive(item);
    if (timeOut) {
      clearTimeout(timeOut);
    }
    timeOut = setTimeout(() => {
      setIsLoading(false);
    }, 500);
  };

  return (
    <div className="nc-SectionMagazine2">
      <HeaderFilter
        tabActive={tabActive}
        tabs={tabs}
        heading={heading}
        onClickTab={handleClickTab}
      />

      {!activePosts.length && <span>Nothing we found!</span>}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        <div className="grid gap-6">
          {activePosts
            .filter((_, i) => i < 3 && i > 0)
            .map((item, index) => {
              return (
                <Card11 ratio="aspect-w-5 aspect-h-3" key={index} post={item} />
              );
            })}
        </div>
        <div className="lg:col-span-2">
          {activePosts[0] && <Card2 size="large" post={activePosts[0]} />}
        </div>
        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-1 md:col-span-3 xl:col-span-1">
          {activePosts
            .filter((_, i) => i < 5 && i >= 3)
            .map((item, index) => {
              return (
                <Card11 ratio="aspect-w-5 aspect-h-3" key={index} post={item} />
              );
            })}
        </div>
      </div>
    </div>
  );
};

export default SectionMagazine2;
