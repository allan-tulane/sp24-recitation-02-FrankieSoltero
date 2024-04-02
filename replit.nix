{ pkgs }: {
  deps = [
    pkgs.run
    pkgs.python310Packages.pytest
    pkgs.python311Packages.pytest
  ];
}