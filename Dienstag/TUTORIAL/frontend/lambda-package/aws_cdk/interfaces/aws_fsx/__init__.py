from __future__ import annotations

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from jsii._type_checking import cached_type_hints, check_type


from ..._jsii import *

class _LazyImport:
    def __init__(self, module_name: str) -> None:
        self._module_name = module_name
        self._module: typing.Any = None
    def __getattr__(self, name: str) -> typing.Any:
        if self._module is None:
            import importlib
            self._module = importlib.import_module(self._module_name)
        return getattr(self._module, name)

if typing.TYPE_CHECKING:

    import aws_cdk.interfaces as _interfaces_8ca7e747
    import constructs as _constructs_77d1e7e8
else:

    _constructs_77d1e7e8 = _LazyImport("constructs")
    _interfaces_8ca7e747 = _LazyImport("aws_cdk.interfaces")


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.BackupReference",
    jsii_struct_bases=[],
    name_mapping={"backup_id": "backupId", "resource_arn": "resourceArn"},
)
class BackupReference:
    def __init__(self, *, backup_id: builtins.str, resource_arn: builtins.str) -> None:
        '''A reference to a Backup resource.

        :param backup_id: The BackupId of the Backup resource.
        :param resource_arn: The ResourceARN of the Backup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fsx as interfaces_fsx
            
            backup_reference = interfaces_fsx.BackupReference(
                backup_id="backupId",
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__428cd57a1881032d6c1c3a479146a90a990148935af981efafe77a557f9ca598)
            check_type(argname="argument backup_id", value=backup_id, expected_type=type_hints["backup_id"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_id": backup_id,
            "resource_arn": resource_arn,
        }

    @builtins.property
    def backup_id(self) -> builtins.str:
        '''The BackupId of the Backup resource.'''
        result = self._values.get("backup_id")
        assert result is not None, "Required property 'backup_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceARN of the Backup resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.DataRepositoryAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_id": "associationId"},
)
class DataRepositoryAssociationReference:
    def __init__(self, *, association_id: builtins.str) -> None:
        '''A reference to a DataRepositoryAssociation resource.

        :param association_id: The AssociationId of the DataRepositoryAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fsx as interfaces_fsx
            
            data_repository_association_reference = interfaces_fsx.DataRepositoryAssociationReference(
                association_id="associationId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1721b2217c8a769d168dd3182f74b58f64a161dc58300822743bdefbab90fc9b)
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_id": association_id,
        }

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the DataRepositoryAssociation resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataRepositoryAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.FileCacheReference",
    jsii_struct_bases=[],
    name_mapping={"file_cache_id": "fileCacheId", "resource_arn": "resourceArn"},
)
class FileCacheReference:
    def __init__(
        self,
        *,
        file_cache_id: builtins.str,
        resource_arn: builtins.str,
    ) -> None:
        '''A reference to a FileCache resource.

        :param file_cache_id: The FileCacheId of the FileCache resource.
        :param resource_arn: The ResourceARN of the FileCache resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fsx as interfaces_fsx
            
            file_cache_reference = interfaces_fsx.FileCacheReference(
                file_cache_id="fileCacheId",
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__eefda58109758b4710ae1e33f42a5bddf728601a65d33d5549088b9f4903957e)
            check_type(argname="argument file_cache_id", value=file_cache_id, expected_type=type_hints["file_cache_id"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_cache_id": file_cache_id,
            "resource_arn": resource_arn,
        }

    @builtins.property
    def file_cache_id(self) -> builtins.str:
        '''The FileCacheId of the FileCache resource.'''
        result = self._values.get("file_cache_id")
        assert result is not None, "Required property 'file_cache_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceARN of the FileCache resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileCacheReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.FileSystemReference",
    jsii_struct_bases=[],
    name_mapping={"file_system_id": "fileSystemId"},
)
class FileSystemReference:
    def __init__(self, *, file_system_id: builtins.str) -> None:
        '''A reference to a FileSystem resource.

        :param file_system_id: The Id of the FileSystem resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fsx as interfaces_fsx
            
            file_system_reference = interfaces_fsx.FileSystemReference(
                file_system_id="fileSystemId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d0a33871199f6693f73a9bdd995bca31d1c63f7798a526d177f21c3a07e0a6e3)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
        }

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''The Id of the FileSystem resource.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fsx.IBackupRef")
class IBackupRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Backup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="backupRef")
    def backup_ref(self) -> "BackupReference":
        '''(experimental) A reference to a Backup resource.

        :stability: experimental
        '''
        ...


class _IBackupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Backup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fsx.IBackupRef"

    @builtins.property
    @jsii.member(jsii_name="backupRef")
    def backup_ref(self) -> "BackupReference":
        '''(experimental) A reference to a Backup resource.

        :stability: experimental
        '''
        return typing.cast("BackupReference", jsii.get(self, "backupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBackupRef).__jsii_proxy_class__ = lambda : _IBackupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.IDataRepositoryAssociationRef"
)
class IDataRepositoryAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataRepositoryAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataRepositoryAssociationRef")
    def data_repository_association_ref(self) -> "DataRepositoryAssociationReference":
        '''(experimental) A reference to a DataRepositoryAssociation resource.

        :stability: experimental
        '''
        ...


class _IDataRepositoryAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataRepositoryAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fsx.IDataRepositoryAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="dataRepositoryAssociationRef")
    def data_repository_association_ref(self) -> "DataRepositoryAssociationReference":
        '''(experimental) A reference to a DataRepositoryAssociation resource.

        :stability: experimental
        '''
        return typing.cast("DataRepositoryAssociationReference", jsii.get(self, "dataRepositoryAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataRepositoryAssociationRef).__jsii_proxy_class__ = lambda : _IDataRepositoryAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fsx.IFileCacheRef")
class IFileCacheRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FileCache.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fileCacheRef")
    def file_cache_ref(self) -> "FileCacheReference":
        '''(experimental) A reference to a FileCache resource.

        :stability: experimental
        '''
        ...


class _IFileCacheRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FileCache.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fsx.IFileCacheRef"

    @builtins.property
    @jsii.member(jsii_name="fileCacheRef")
    def file_cache_ref(self) -> "FileCacheReference":
        '''(experimental) A reference to a FileCache resource.

        :stability: experimental
        '''
        return typing.cast("FileCacheReference", jsii.get(self, "fileCacheRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFileCacheRef).__jsii_proxy_class__ = lambda : _IFileCacheRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fsx.IFileSystemRef")
class IFileSystemRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FileSystem.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fileSystemRef")
    def file_system_ref(self) -> "FileSystemReference":
        '''(experimental) A reference to a FileSystem resource.

        :stability: experimental
        '''
        ...


class _IFileSystemRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FileSystem.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fsx.IFileSystemRef"

    @builtins.property
    @jsii.member(jsii_name="fileSystemRef")
    def file_system_ref(self) -> "FileSystemReference":
        '''(experimental) A reference to a FileSystem resource.

        :stability: experimental
        '''
        return typing.cast("FileSystemReference", jsii.get(self, "fileSystemRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFileSystemRef).__jsii_proxy_class__ = lambda : _IFileSystemRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fsx.IS3AccessPointAttachmentRef")
class IS3AccessPointAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a S3AccessPointAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="s3AccessPointAttachmentRef")
    def s3_access_point_attachment_ref(self) -> "S3AccessPointAttachmentReference":
        '''(experimental) A reference to a S3AccessPointAttachment resource.

        :stability: experimental
        '''
        ...


class _IS3AccessPointAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a S3AccessPointAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fsx.IS3AccessPointAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="s3AccessPointAttachmentRef")
    def s3_access_point_attachment_ref(self) -> "S3AccessPointAttachmentReference":
        '''(experimental) A reference to a S3AccessPointAttachment resource.

        :stability: experimental
        '''
        return typing.cast("S3AccessPointAttachmentReference", jsii.get(self, "s3AccessPointAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IS3AccessPointAttachmentRef).__jsii_proxy_class__ = lambda : _IS3AccessPointAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fsx.ISnapshotRef")
class ISnapshotRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Snapshot.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="snapshotRef")
    def snapshot_ref(self) -> "SnapshotReference":
        '''(experimental) A reference to a Snapshot resource.

        :stability: experimental
        '''
        ...


class _ISnapshotRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Snapshot.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fsx.ISnapshotRef"

    @builtins.property
    @jsii.member(jsii_name="snapshotRef")
    def snapshot_ref(self) -> "SnapshotReference":
        '''(experimental) A reference to a Snapshot resource.

        :stability: experimental
        '''
        return typing.cast("SnapshotReference", jsii.get(self, "snapshotRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISnapshotRef).__jsii_proxy_class__ = lambda : _ISnapshotRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fsx.IStorageVirtualMachineRef")
class IStorageVirtualMachineRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StorageVirtualMachine.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="storageVirtualMachineRef")
    def storage_virtual_machine_ref(self) -> "StorageVirtualMachineReference":
        '''(experimental) A reference to a StorageVirtualMachine resource.

        :stability: experimental
        '''
        ...


class _IStorageVirtualMachineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StorageVirtualMachine.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fsx.IStorageVirtualMachineRef"

    @builtins.property
    @jsii.member(jsii_name="storageVirtualMachineRef")
    def storage_virtual_machine_ref(self) -> "StorageVirtualMachineReference":
        '''(experimental) A reference to a StorageVirtualMachine resource.

        :stability: experimental
        '''
        return typing.cast("StorageVirtualMachineReference", jsii.get(self, "storageVirtualMachineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStorageVirtualMachineRef).__jsii_proxy_class__ = lambda : _IStorageVirtualMachineRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fsx.IVolumeRef")
class IVolumeRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        ...


class _IVolumeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fsx.IVolumeRef"

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        return typing.cast("VolumeReference", jsii.get(self, "volumeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVolumeRef).__jsii_proxy_class__ = lambda : _IVolumeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.S3AccessPointAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"s3_access_point_attachment_name": "s3AccessPointAttachmentName"},
)
class S3AccessPointAttachmentReference:
    def __init__(self, *, s3_access_point_attachment_name: builtins.str) -> None:
        '''A reference to a S3AccessPointAttachment resource.

        :param s3_access_point_attachment_name: The Name of the S3AccessPointAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fsx as interfaces_fsx
            
            s3_access_point_attachment_reference = interfaces_fsx.S3AccessPointAttachmentReference(
                s3_access_point_attachment_name="s3AccessPointAttachmentName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e7b69ad480bd3986298df21c8960981ce7acf3e4e3a690a221cb9fa219eb1e65)
            check_type(argname="argument s3_access_point_attachment_name", value=s3_access_point_attachment_name, expected_type=type_hints["s3_access_point_attachment_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_access_point_attachment_name": s3_access_point_attachment_name,
        }

    @builtins.property
    def s3_access_point_attachment_name(self) -> builtins.str:
        '''The Name of the S3AccessPointAttachment resource.'''
        result = self._values.get("s3_access_point_attachment_name")
        assert result is not None, "Required property 's3_access_point_attachment_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3AccessPointAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.SnapshotReference",
    jsii_struct_bases=[],
    name_mapping={"snapshot_id": "snapshotId"},
)
class SnapshotReference:
    def __init__(self, *, snapshot_id: builtins.str) -> None:
        '''A reference to a Snapshot resource.

        :param snapshot_id: The Id of the Snapshot resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fsx as interfaces_fsx
            
            snapshot_reference = interfaces_fsx.SnapshotReference(
                snapshot_id="snapshotId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__050d9d405c475bcb5f2999f68089075cc8c795ac3b96823f7b5a6af5812769c9)
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "snapshot_id": snapshot_id,
        }

    @builtins.property
    def snapshot_id(self) -> builtins.str:
        '''The Id of the Snapshot resource.'''
        result = self._values.get("snapshot_id")
        assert result is not None, "Required property 'snapshot_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnapshotReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.StorageVirtualMachineReference",
    jsii_struct_bases=[],
    name_mapping={"storage_virtual_machine_id": "storageVirtualMachineId"},
)
class StorageVirtualMachineReference:
    def __init__(self, *, storage_virtual_machine_id: builtins.str) -> None:
        '''A reference to a StorageVirtualMachine resource.

        :param storage_virtual_machine_id: The StorageVirtualMachineId of the StorageVirtualMachine resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fsx as interfaces_fsx
            
            storage_virtual_machine_reference = interfaces_fsx.StorageVirtualMachineReference(
                storage_virtual_machine_id="storageVirtualMachineId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4c3b13daf1ed04abe471acb64003f29823aa258b5808489f7e3ec0e2d69c6875)
            check_type(argname="argument storage_virtual_machine_id", value=storage_virtual_machine_id, expected_type=type_hints["storage_virtual_machine_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_virtual_machine_id": storage_virtual_machine_id,
        }

    @builtins.property
    def storage_virtual_machine_id(self) -> builtins.str:
        '''The StorageVirtualMachineId of the StorageVirtualMachine resource.'''
        result = self._values.get("storage_virtual_machine_id")
        assert result is not None, "Required property 'storage_virtual_machine_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageVirtualMachineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fsx.VolumeReference",
    jsii_struct_bases=[],
    name_mapping={"volume_id": "volumeId"},
)
class VolumeReference:
    def __init__(self, *, volume_id: builtins.str) -> None:
        '''A reference to a Volume resource.

        :param volume_id: The VolumeId of the Volume resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fsx as interfaces_fsx
            
            volume_reference = interfaces_fsx.VolumeReference(
                volume_id="volumeId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__61f38b8d84730ff5f4ebf7e7fea2aba7014e031fcdb9669434a022fbac741c6e)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The VolumeId of the Volume resource.'''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BackupReference",
    "DataRepositoryAssociationReference",
    "FileCacheReference",
    "FileSystemReference",
    "IBackupRef",
    "IDataRepositoryAssociationRef",
    "IFileCacheRef",
    "IFileSystemRef",
    "IS3AccessPointAttachmentRef",
    "ISnapshotRef",
    "IStorageVirtualMachineRef",
    "IVolumeRef",
    "S3AccessPointAttachmentReference",
    "SnapshotReference",
    "StorageVirtualMachineReference",
    "VolumeReference",
]

publication.publish()

def _typecheckingstub__428cd57a1881032d6c1c3a479146a90a990148935af981efafe77a557f9ca598(
    *,
    backup_id: builtins.str,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1721b2217c8a769d168dd3182f74b58f64a161dc58300822743bdefbab90fc9b(
    *,
    association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eefda58109758b4710ae1e33f42a5bddf728601a65d33d5549088b9f4903957e(
    *,
    file_cache_id: builtins.str,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a33871199f6693f73a9bdd995bca31d1c63f7798a526d177f21c3a07e0a6e3(
    *,
    file_system_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b69ad480bd3986298df21c8960981ce7acf3e4e3a690a221cb9fa219eb1e65(
    *,
    s3_access_point_attachment_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__050d9d405c475bcb5f2999f68089075cc8c795ac3b96823f7b5a6af5812769c9(
    *,
    snapshot_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3b13daf1ed04abe471acb64003f29823aa258b5808489f7e3ec0e2d69c6875(
    *,
    storage_virtual_machine_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61f38b8d84730ff5f4ebf7e7fea2aba7014e031fcdb9669434a022fbac741c6e(
    *,
    volume_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBackupRef, IDataRepositoryAssociationRef, IFileCacheRef, IFileSystemRef, IS3AccessPointAttachmentRef, ISnapshotRef, IStorageVirtualMachineRef, IVolumeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
